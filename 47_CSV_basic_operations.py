import csv

# getting data from CSV

example_csv_file = open('fruits.csv')

example_csv_reader = csv.reader(example_csv_file)
example_python_data = list(example_csv_reader)

example_csv_file.close()


# writing data to CSV

output_csv_file = open('fruits2.csv', 'w')

output_csv_writer = csv.writer(output_csv_file, delimiter='\t', lineterminator='\n\n')

for row in example_python_data:
    output_csv_writer.writerow(row)

output_csv_file.close()
