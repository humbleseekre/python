'''
You're goal for this challenge is to write a function to save a Python dictionary object to file. Your save function
should take two input arguments for the dictionary to save and an output file path. Now, saved data is only useful
if you can retrieve it later, so you should also write a second function to load the saved dictionary back into Python.
That load function should take a file path, to the saved dictionary as it's input and then return the retrieved
dictionary object.
'''


'''
When you need to preserve something for later, you pickle it. So that's what I did for 
my solution. In Python pickling is a process which serializes a Python object, converting it into a byte stream, 
that can be saved to file. The inverse operation of unpick ling can then be used to later deserialize the byte stream 
back into the original object structure. Python's pickle module provides the interface to pickle and un-pickle objects
pickle: Python object serialization. Pickle module implements binary protocols for serializing and de-serializing a 
Python object structure. "Pickling is the process whereby a Python object hierarchy is converted into a byte stream,
and "unpickling" is the inverse operation, whereby a byte stream (from a binary file or byte-like object) is converted
back into an object hierarchy. Pickling (and unpickling) is alternatively known as "serialization", "marshalling" or 
"flattening".
'''

import pickle

def save_dict(dict_to_save, file_path):
    #open a file to write binary data
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)


def load_dict(file_path):
    # open file to read binary data
    with open(file_path, 'rb') as file:
        return pickle.load(file)




