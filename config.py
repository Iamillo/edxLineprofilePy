source_directory = '.\\source\\'
results_directory = '.\\results\\'

input_file_header = {'x': [],
                     'Ni': [],
                     'Co': [],
                     'Ru': []}
colors = {'Ni': 'blue',
          'Co': 'green',
          'Ru': 'red'}
elements = list(colors.keys())

# converting concentrations from Mol/Mol into at. in %
con_unit_conversion_factor = 1.e2
# converting x-axis from m into nm
x_unit_conversion_factor = 1.e9
