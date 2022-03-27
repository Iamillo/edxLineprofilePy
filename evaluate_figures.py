import os

import matplotlib.pyplot as mapy

import config
from config import colors
from filter import savgol_filter
from plotting import plotAttime


def evaluate_print_figures(values: dict, eval_time: list, elements: list) -> None:
    number_subplots = len(eval_time) * len(elements)
    fig, axs = mapy.subplots(len(eval_time),
                            len(elements),
                            sharex='col',
                            sharey='col',
                            gridspec_kw={'hspace':0, 'wspace':0.25})
    fig.suptitle("time", x=.94)

    for e in range(0, len(elements)):
        elem = elements[e]
        axs[0, e].set_title(elem[0].upper()+elem[1])
        axs[len(eval_time)-1, e].set_xlabel('x / nm', fontsize=20)
        axs[len(eval_time) - 1, e].set_xticks([0,30,60,90])
        for t in range(0, len(eval_time)):
            time = list(eval_time)[t]
            axs[t, e].set_xlim(0, 90)
            axs[t, e].plot(values[time]['x'], values[time][elem], ':', color='lightgray')  # , marker, label=elem + time)
            axs[t, e].plot(values[time]['x'], savgol_filter(values[time][elem]), color=colors[elem])#, marker, label=elem + time)

            if e == 2:
                axs[t, e].text(100, 9, str(int(time.replace('sec',''))) + ' s', fontsize=20)
    #        if e == 0:
    #            axs[t, e].set_yticks([35, 50])
    #        if e == 1:
    #            axs[t, e].set_yticks([41, 45])
    #        if e == 2:
    #            axs[t, e].set_yticks([7, 12])
            if e == 0 and t == round(len(eval_time) /2)-1:
                axs[t, e].set_ylabel('c / at.%', fontsize=20)
            axs[t, e].tick_params(labelsize=15)

    fig.savefig(os.path.join(config.results_directory, '3E_col.png'), dpi=300)
    mapy.show()

def delta(position, peaksOverTime=None, deviationOverTime=None):
    # plotting delta c = c_twin - c_matrix VS time
    # not in use at the moment
    f1 = mapy.figure(1)

    for elem in ['Ni','Co','Ru']:
        #mapy.yscale('log')
        mapy.plot(peaksOverTime['sec'],
                  peaksOverTime[elem],
                  '--o',
                  label=(elem[0].upper()+elem[1]), color=colors[elem])
        mapy.errorbar(deviationOverTime['sec'],
                      peaksOverTime[elem],
                      deviationOverTime[elem],
                      elinewidth=1,
                      capsize=2,
                      linestyle='None',
                      color='grey')
        mapy.grid(linestyle=':', linewidth='0.5', color='grey')
        mapy.legend()
        mapy.ylabel(r'$\Delta c = C_{twin}-C_{matrix}$', fontsize=15)
        mapy.xlabel('t in s', fontsize=15)


def dummy(position, eval_time, c_init, elem):
    # plotting c VS x for all times
    # not in use at the moment
    for time in eval_time:
        f2 = mapy.figure(2)
        plotAttime(position, time, marker='x', elems='Co')
        plotAttime(position, time, marker='-', elems='Co', filter='savgolFilter')
        mapy.plot([min(position[time]['x']), max(position[time]['x'])],
                  [c_init[time]['Co'], c_init[time]['Co']],
                  '--',
                  label=elem+time+'init')
    mapy.xlim(left=0.0)
    mapy.xlim(right=90.0)
