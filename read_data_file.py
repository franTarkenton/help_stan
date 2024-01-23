data_file = 'exoplanet_2024A_data.txt'

# open up the file listed above for reading


def read_file():
    """opens the file 'data_file' and prints each line to the screen
    """
    fh = open(data_file, 'r')
    for line in fh:
        print(line)
    fh.close()

# def read_file2():
#     """opens the file 'data_file' and extracts the column names from 
#     the file
#     """
#     with open(data_file, 'r') as fh:

#         for line in fh:
#            if line.startswith('Column'):
#                print(line)
#             elif line.startswith('Exoplanet')
           

pressure = [[1], [150.000, 151, 153.000], ]
temperature = [[1], [165.84, 166.35, 166.85]]

data = {
    1: {
        'pressure': [150.000, 151, 153.000],
        'temperature': [165.84, 166.35, 166.85]
    }
}

print(f'station 1 pressure values are: {data[1]["pressure"]}' )
print(f'station 1 temp values are: {data[1]["temperature"]}' )

import matplotlib.pyplot as plt
plt.scatter(data[1]["temperature"], data[1]["pressure"], label= "stars", color= "green", 
            marker= "*", s=30)

plt.savefig('junk.png')




# print(pressure[1])



#read_file()
