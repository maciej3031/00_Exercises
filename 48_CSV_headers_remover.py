import csv, os

# removing header from CSV

os.makedirs('Removed_headers', exist_ok=True)       # creating folder for new CSV files without headers

for csv_file in os.listdir('.'):            # loop through every file in current directory
    if not csv_file.endswith('.csv'):       # skip any other files than .csv
        continue
    print('Removing header from ', csv_file)

    csv_file_object = open(csv_file)            # open csv file
    csv_reader = csv.reader(csv_file_object)    # read csv file to csv_reader object

    csv_rows = []
    for row in csv_reader:              # loop through every row in csv_reader object
        if csv_reader.line_num == 1:    # skip first row
            continue
        csv_rows.append(row)            # all rows except the first append to csv_rows[] list

    csv_file_object.close()             # close old csv file

    csv_output_file = open(os.path.join('Removed_headers', csv_file), 'w')      # create new csv file in new folder
    csv_witer = csv.writer(csv_output_file)     # create csv_writer object

    for row in csv_rows:
        csv_witer.writerow(row)         # write every row of list to new csv file

    csv_output_file.close()             # close new csv file
