[![Python 3.8](https://img.shields.io/badge/Python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Matplotlib 3.5.1](https://img.shields.io/badge/Matplotlib-3.5.1-green.svg)](https://matplotlib.org/)
[![NumPy 1.20.1](https://img.shields.io/badge/NumPy-1.20.1-red.svg)](https://numpy.org/devdocs/index.html)
[![SciPy 1.8.0](https://img.shields.io/badge/SciPy-1.8.0-yellow.svg)](https://scipy.org/)
[![statsmodels 0.13.2](https://img.shields.io/badge/statsmodels-0.13.2-purple.svg)](https://www.statsmodels.org/stable/index.html)

# edxLineprofilePy
This is a simple evaluation tool to plot edx line profile results in Python.

This little piece of code has been written with very little effort in time and therefore will
require adaptions for specific usages.

Fixes and enhancements are highly welcome !

### How to use
1. Prepare input data:  
   The input files read are expected in a subdirectory <b>source</b> which needs to be created in the root directory 
   of this repository. All files need to be <u>semicolon separated</u> csv files with a header as follows  

    | x    | Ni       | Ru      | Co     | ... |
    |------|----------|---------|--------|-----|
    |values| values   | values  | values |     |
    
    Note:
    - the header must contain the column `x`
    - all other columns are optional, depending on what data you want to process
    - the columns specified in the configuration in `config.py` have to be available in all input files
    - the order of the columns is irrelevant
    - the capitalization of column names is important between the input files and the configuration in `config.py`, 
      i.e. "Ni" and "ni" are not the same
    
    Moreover, the filenames need to start with two digits representing the time in seconds the data set
    belongs to. Files not matching this file name criteria are going to be ignored. 
    Besides from that, you can place as many files into the source directory as you want.


2. Set configuration if necessary  
   In `config.py` you can change some configuration:
   - change name of source directory
   - change name of results directory
   - add / remove elements of the input file header, note that these are the elements which will be processed
     by the program, the configuration does not necessarily need to list all elements available in the input 
     file headers
   - elementwise define colors for the output plots


### Execute the program
After preparing the input files and setting up the configuration, the
program can be executed by running `evaluation_master.py`.

### Example
The directory `Example` contains two example input csv files.
In order to use them, copy the files into the `source` directory you
created into the root directory of this repository 
(see [How to use instructions](#how-to-use) above). 

### Required software and packages
This program has been implemented and tested on Python 3.8.  
Moreover, the following additional packages are required:
- Matplotlib 3.5.1
- SciPy 1.8.0
- NumPy 0.20.1
- statsmodels 0.13.2

It is recommended to use an [integrated development environment (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment) 
like the [PyCharm Community Edition](https://www.jetbrains.com/pycharm/). PyCharm comes with an Python 3.X installation and among many 
other convenient features, includes a package manager which can be used to install the above mentioned required packages. For more details
see the [documations](https://www.jetbrains.com/help/pycharm/quick-start-guide.html).

### Contribute
All kind of contribution is highly welcome, no matter if bug fix, enhancement
or improvement of the (due to lack of time) very simple coding quality.
