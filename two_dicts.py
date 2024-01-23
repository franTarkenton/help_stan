
import re
import pprint
import json
import copy
import random

column_names = [
    'probe', 
    'pressure',
    'temperature',
    'density',
    'density_n2',
    'density_he',
    'density_ar',
    'density_co2',
    'altitude'
]



def read_file(filename: str):
    """opens the file 'data_file' and prints each line to the screen
    """
    data_struct = {}
    if filename is None:
        print('No filename given')
        return
    # read the header to get the colum
    at_data = False
    with open(filename, 'r') as fh:
        for line in fh:
            # strip any whitespace from the line and look for the 
            # blank line in between the column defs and the actual data
            line = line.strip()
            if at_data:
                data_list = re.split('\s+', line)
                cnt = 0
                probe = data_list[0]
                if probe not in data_struct:
                    data_struct[probe] = {}
                for col_position in range(1, len(column_names)):
                    col_name = column_names[col_position]
                    if col_name not in data_struct[probe]:
                        data_struct[probe][col_name] = []
                for col_position in range(1, len(column_names)):
                    col_name = column_names[col_position]
                    data_struct[probe][col_name].append(data_list[col_position])
            elif not line:
                at_data = True
                continue
    
    # pp =  pprint.PrettyPrinter(indent=4)
    # pp.pprint(data_struct)
    return data_struct

def demo_two_dicts(dict1, dict2):
    for probe in dict1:
        for col_name in dict1[probe]:
            cnt = 0
            for data in dict1[probe][col_name]:
                value_dict1 = data
                # corresponding value in dictionary 2 for the same column name
                # and array position
                value_dict2 = dict2[probe][col_name][cnt]
                cnt += 1
            
def save(struct, output_file):
    """saves the data structure to a file
    """
    with open(output_file, 'w') as fh:
        json.dump(struct, fh, indent=4)
            
def mangle(struct):
    """mangles the data structure, by replaceing the values with random values
    """
    for probe in struct:
        for col_name in struct[probe]:
            cnt = 0
            for data in struct[probe][col_name]:
                struct[probe][col_name][cnt] = random.randint(0, 1000)
                cnt += 1
    return struct


if __name__ == '__main__':
    exo_file = 'exoplanet_2024A_data.txt'
    tmp_json = 'json_data.json'
    mangled_data = 'mangled.json'

    data_struct = read_file(filename=exo_file)
    save(data_struct, tmp_json)

    new_dict = copy.deepcopy(data_struct)
    mangled_dict = mangle(new_dict)
    save(mangled_dict, mangled_data)

    demo_two_dicts(data_struct, new_dict)

