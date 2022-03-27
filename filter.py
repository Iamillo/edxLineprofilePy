from statsmodels.nonparametric.smoothers_lowess import lowess
from scipy.signal import lfilter
from scipy.signal import savgol_filter as sf


def lowess_filter(x, dat):
    filtered = lowess(dat, x, is_sorted=True, frac=0.025, it=0)
    return filtered[:, 0], filtered[:, 1]


def l_filter(dat):
    n = 40
    b = [1.0 / n] * n
    a = 1
    return lfilter(b, a, dat)


def savgol_filter(dat):
    return sf(dat, 91, 7)
