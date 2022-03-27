import csv
import os
from copy import deepcopy

import config
from evaluate_figures import evaluate_print_figures
from filter import savgol_filter

from tools import (
    shift_x,
    get_init_concentrations,
    get_deviation,
    get_all_peak_positions
)


def find_input_files(dir: str) -> dict:
    found_files = {}
    for f in os.listdir(dir):
        try:
            int(f[0:2])
        except ValueError as e:
            print(f"Ignoring file {f} as it can not be matched to a time position.")
            print(e)
            continue
        found_files[f[0:2]] = f
    return found_files


file_names = find_input_files(config.source_directory)

# read data into dictionary #################################################################
#############################################################################################

position = {}
# iterating through csv files
for time_position, filename in file_names.items():
    position[time_position] = deepcopy(config.input_file_header)

    with open(os.path.join(config.source_directory, filename), 'r') as csvfile:
        content = csv.DictReader(csvfile, delimiter=';')
        counter = 0
        # iterating through the lines of a csv file
        for line in content:
            counter += 1
            try:
                scaleX = 1.e9
                # iterating through the columns of a
                for csv_column in config.input_file_header:
                    # the cast to float is important,
                    # 1) csv might be interpreted as string,
                    # 2) skips lines between header and first values
                    position[time_position][csv_column].append(scaleX * float(line[csv_column]))
            except ValueError:
                # skipping lines describing header and units, etc.
                continue

position = shift_x(position, center=45.0)
c_init = get_init_concentrations(position, center=45.0, peakWidth=15.0)
c_deviation = get_deviation(position, center=45.0, peakWidth=15.0)

peakPos = get_all_peak_positions(position)

eval_time = position.keys()
elements = ['Ni', 'Co', 'Ru']
peaksOverTime = {'sec':[]}
deviationOverTime = {'sec':[]}
for time in eval_time:
    peaksOverTime['sec'].append(int(time))
    deviationOverTime['sec'].append(int(time))
for elem in ['Ni', 'Co', 'Ru']:
    peaksOverTime[elem] = []
    deviationOverTime[elem] = []
    for time in eval_time:
        peakIndex = position[time]['x'].index(peakPos[time])
        filtered = savgol_filter(position[time][elem])
        peaksOverTime[elem].append(filtered[peakIndex] - c_init[time][elem])

        deviationOverTime[elem].append(c_deviation[elem][c_deviation['sec'].index(int(time[0:2]))])


evaluate_print_figures(position, eval_time, elements)
