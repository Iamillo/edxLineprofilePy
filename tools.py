import numpy as np

from filter import (
    lowess_filter,
    l_filter,
    savgol_filter
)


def get_peak_pos(values: dict, time: str, elem: str, filter: str =None) -> dict:
    if filter == 'lowessFilter':
        elem_values = lowess_filter(values[time]['x'], values[time][elem])[1].tolist()
    elif filter == 'lFilter':
        elem_values = l_filter(values[time][elem]).tolist()
    elif filter == 'savgolFilter':
        elem_values = savgol_filter(values[time][elem]).tolist()
    else:
        elem_values = values[time][elem]
    if elem == 'Ni':
        idx = elem_values.index(min(elem_values))
    elif elem in ['Co', 'Ru']:
        idx = elem_values.index(max(elem_values))
    return values[time]['x'][idx]


def get_all_peak_positions(values: dict) -> dict:
    # getting peak positions on 'savgol'-filtered data for 'Ru'
    peakPos = {}
    for time in values:
        for elem in ['Ru']:
            peakPos[time] = get_peak_pos(values, time, elem, filter='lowessFilter')
    return peakPos


def shift_x(values, center):
    # displace all peaks to x = 45 ! ! !
    peakPos = get_all_peak_positions(values)
    for time in values:
        deltaToX = peakPos[time] - center
        for x in range(0, len(values[time]['x'])):
            values[time]['x'][x] -= deltaToX
    return values


def get_deviation(values, center, peakWidth):
    c_deviations = {'sec' : [int(x[0:2]) for x in list(values.keys())]}
    for elem in ['Ni', 'Co', 'Ru']:
        c_deviations[elem] = []
        for time in values:
            temp_list = [values[time][elem][x]
                         for x in range(0, len(values[time][elem]))
                         if abs(values[time]['x'][x] - center) > peakWidth]
            temp_list = np.asarray(temp_list, dtype=np.float32)
            c_deviations[elem].append(temp_list.std())
    return c_deviations


def get_init_concentrations(values, center, peakWidth):
    c_init = {}
    for time in values:
        c_init[time] = {}
        for elem in ['Ni', 'Co', 'Ru']:
            c_init[time][elem] = 0.0
            counter = 0
            for x in range(0, len(values[time]['x'])):
                if abs(values[time]['x'][x] - center) > peakWidth:
                    counter += 1
                    c_init[time][elem] += values[time][elem][x]
            c_init[time][elem] /= counter
    return c_init
