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

### Required packages
- matplotlib
- scipy
- numpy
- statsmodels

### Contribute
All kind of contribution is highly welcome, no matter if bug fix, enhancement
or improvement of the (due to lack of time) very simple coding quality.
