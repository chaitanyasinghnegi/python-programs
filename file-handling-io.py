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

Example for a binary code to read and display its contents:
import struct

# Write binary data to a file
with open('binary_data.bin', 'wb') as binary_file:
    binary_file.write(struct.pack('iid', 123, 45.67, 89.12))

# Read binary data from the file
with open('binary_data.bin', 'rb') as binary_file:
    data = struct.unpack('iid', binary_file.read())

# Display the data
labels = ["Integer", "Float 1", "Float 2"]
for label, value in zip(labels, data):
    print(f"{label}: {value}")

"""
reading a CSV File
"""
import csv
csv_file_path = 'path/to/your/csvfile.csv'
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)



