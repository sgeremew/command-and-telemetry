# gps.py
# 
# Flight Command and Telemetry
# 
# GPS Objective: 
# >recieve a csv file containing gps data, from Sensor Collection Team such as: 
#  latitude, longitude, altitude
# 
# >parse the csv file to get data
# 
# >then telemetry peeps will store this data into telemetry records to broadcast 
#  this data to the ground team
# 


import csv

# Need to figure out how the Sensor team is sending the csv file and how we 
# are recieving it.

# TESTING: using this file to test csv reading and output

#filename = 'gps_test.csv'
#filename = 'BalloonFlightDataWorking2.csv'
filename = 'sdata.csv'
#filename = input("\tgimme a csv file now\n")

# This dictionary holds the data for each position read
positions = {}

##############################################################################
# opens the csv file
# 
# Treating each row as a snapshot of the position captured. Then the data is 
# stored into a dictionary where the keys are the position and the values are 
# the list of data points such as latitude, longitude, etc.
#
# The data that is stored in the dictionary will be adjusted to how the Sensor 
# team stores it.
names = []
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # PRINT for testing purposes
            # note: str.join(sequence) joins the data in the sequence row 
            #       and separates them using str (in our case the string  ", ")
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # dict.update(key:value) adds a new key:value pair to the dictionary
            positions.update({line_count-1:row})
            
            # PRINT for testing purposes
            # note: the print(f'print me') function uses f-string which allows 
            #       for formatting where using curly brackets allow variables
            #       This is similar to using str.format().
            # print(f'\tPosition({line_count-1}):\tLatitude\t{row[0]}\n'
            #                                 f'\t\t\tLongitude\t{row[1]}')
            # print('\t---------------------------------------------')

            line_count += 1
    print(f'Processed {line_count} lines.\n')
# PRINT for testing purposes
print(positions)
