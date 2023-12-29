"""
reading a text file
"""
with open("text.txt",w) as file_object:
  rd=file_object.read()

"""
reading a binary file 
"""
# binary_file_path = 'path/to/your/binaryfile.bin'
 with open(binary_file_path, 'rb') as binary_file:
        # Read the entire binary file into a bytes object
        binary_data = binary_file.read()

