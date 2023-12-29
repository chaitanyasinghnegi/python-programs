"""
reading a text file
"""
with open("text.txt",w) as file_object:
  rd=file_object.reader()

"""
reading a binary file 
"""
# binary_file_path = 'path/to/your/binaryfile.bin'
 with open(binary_file_path, 'rb') as binary_file:
        # Read the entire binary file into a bytes object
        binary_data = binary_file.read()

"""
reading a CSV File
"""
import csv
csv_file_path = 'path/to/your/csvfile.csv'
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)



