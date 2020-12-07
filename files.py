import os
import csv
import datetime


if __name__ == '__main__':

    i_path = 'input/'
    o_path = '../output/'

    files_name = os.listdir(i_path)  # Get all the files/folder from the given path

    os.chdir(i_path)  # Change path to the input directory

    for file in files_name:
        if os.path.isfile(file) and file.endswith('.csv'):
            # Get file name and its extension
            name, ext = os.path.splitext(file)
            # Set output file name with current date and time
            output_file_name = name + '_output_' + str(datetime.datetime.now().replace(microsecond=0)) + '.csv'
            # Open output file in write mode
            output_file = csv.writer(open(o_path + output_file_name, 'w+', newline=''), delimiter="|")

            with open(file, mode='r') as csv_file:
                reader = csv.reader(csv_file)
                for line in reader:
                    output_file.writerow(line)

