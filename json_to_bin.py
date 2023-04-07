'''
In this example, we use the json module to load the data from the JSON file into a Python object. 
We then use the json.dumps() method to encode the data as a JSON string, and then use the encode() 
method to convert the string to binary data. Finally, we write the binary data to a new file using 
the open() function with the wb (write binary) mode.
'''

import json

# Open the JSON file
with open('example.json', 'r') as json_file:
    # Load the JSON data
    data = json.load(json_file)

# Encode the JSON data as binary
binary_data = json.dumps(data).encode('utf-8')

# Write the binary data to a new file
with open('example.bin', 'wb') as bin_file:
    bin_file.write(binary_data)
