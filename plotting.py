import matplotlib.pyplot as mapy

from filter import lowess_filter, l_filter
from filter import savgol_filter


def plotPeaks(time, elems):
    peakPos = getAllPeakPositions()
    if type(elems) == str:
        elems = [elems]
    for elem in elems:
        plotAttime(time, elems=elems)
        mapy.plot(peakPos[time], pos1[time][elem][pos1[time]['x'].index(peakPos[time])], color='red', marker='o' )

def plotAll(pos1):
    for time in times:
        for elem in ['ni','co','ru']:
            mapy.plot(pos1[time]['x'],pos1[time][elem],label=elem+time)
    mapy.legend()
    mapy.ylabel('c in at.%')
    mapy.xlabel('x in nm')



def plotAttime(values, time, marker, elems=['Ni', 'Co', 'Ru'], filter=None):
    if type(elems) == str:
        elems = [elems]
    for elem in elems:
        if filter == 'lFilter':
            mapy.plot(values[time]['x'], l_filter(values[time][elem]), marker, label=elem + time)
        elif filter == 'lowessFilter':
            filtered = lowess_filter(values[time]['x'], values[time][elem])
            mapy.plot(filtered[0], filtered[1], marker, label=elem + time)
        elif filter == 'savgolFilter':
            mapy.plot(values[time]['x'], savgol_filter(values[time][elem]), marker, label=elem + time)
        else:
            mapy.plot(values[time]['x'], values[time][elem], marker, label=elem + time)
    mapy.legend()
    mapy.ylabel('c in at.%')
    mapy.xlabel('x in nm')


def compareFilters(time, elems=['ni','co','ru']):
    plotAttime(time, elems=elems)
    #plotAttime(time, elems=elems, filter='lowessFilter')
    #lFilter ist ungeeignet
    #plotAttime(time, elems=elems,filter='lFilter')
    plotAttime(time, elems=elems,filter='savgolFilter')
    mapy.show()