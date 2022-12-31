# Operating System Interface¶
import os
# For daily file and directory management tasks, the shutil module provides a higher level
# interface that is easier to use
import shutil
# File Wildcards¶
import glob
# Command Line Arguments¶
import sys

if __name__ == '__main__':
    # Return the current working directory
    print(f"current working directory is {os.getcwd()}")

    # The glob module provides a function for making file lists from directory wildcard searches:
    print(f"{glob.glob('*.py')}")

    # For daily file and directory management tasks, the shutil module provides a higher level
    # interface that is easier to use:
    shutil.copyfile('test.py', 'test_copy.py')
    shutil.move('test_copy.py', 'test_copy_mv.py')

    # Common utility scripts often need to process command line arguments. 
    # These arguments are stored in the sys module’s argv attribute as a list. For instance the 
    # following output results from running python demo.py one two three at the command line:
    print(f'{sys.argv}')
