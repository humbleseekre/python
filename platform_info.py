import platform


if __name__ == '__main__':

    # displaying platform processor
    print('Platform processor:', platform.processor())

    # returns information about the bit architecture
    print('Platform architecture:', platform.architecture())

    print('uname:', platform.uname())

    print
    print('system   :', platform.system())
    print('node     :', platform.node())
    print('release  :', platform.release())
    print('version  :', platform.version())
    print('machine  :', platform.machine())
    print('processor:', platform.processor())

    print("platform machine: ", platform.machine())
    # returns the machine type, e.g. ‘i386’.

    print("platform node: ", platform.node())
    # returns the computer’s network name (may not be fully qualified!)

    print("platform platform: ", platform.platform())
    # returns a single string identifying the underlying platform with as much useful
    # information as possible.

    print("platform processor: ", platform.processor())
    # returns the (real) processor name, e.g. ‘amdk6’.

    print("platform python build: ", platform.python_build())
    # returns a tuple (buildno, builddate) stating the Python build number and
    # date as strings.

    print("platform python compiler:", platform.python_compiler())
    # returns a string identifying the compiler used for compiling Python.

    print("platform python version:", platform.python_version())
    # returns the Python version as string ‘major.minor.patchlevel’

    print("platform python implmentation:", platform.python_implementation())
    # returns a string identifying the Python implementation.
    # Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’.

    print("platform release: ", platform.release())
    # returns the system’s release, e.g. ‘2.2.0’ or ‘NT’

    print("platform system: ", platform.system())
    # returns the system/OS name, e.g. ‘Linux’, ‘Windows’, or ‘Java’.

    print("platform version: ", platform.version())
    # returns the system’s release version, e.g. ‘#3 on degas’

    print("uname: ", platform.uname())
    # returns a tuple of strings (system, node, release, version, machine, processor)
    # identifying the underlying platform.

    
    
#    output:
#     /Users/neil/venv/bin/python3 /Users/neil/Programming/Python/test_python/test.py -x 1 -y 2
# Platform processor: i386
# Platform architecture: ('64bit', '')
# uname: uname_result(system='Darwin', node='Nilendras-MBP', release='22.1.0', version='Darwin Kernel Version 22.1.0: Sun Oct  9 20:14:54 PDT 2022; root:xnu-8792.41.9~2/RELEASE_X86_64', machine='x86_64', processor='i386')
# system   : Darwin
# node     : Nilendras-MBP
# release  : 22.1.0
# version  : Darwin Kernel Version 22.1.0: Sun Oct  9 20:14:54 PDT 2022; root:xnu-8792.41.9~2/RELEASE_X86_64
# machine  : x86_64
# processor: i386
# platform machine:  x86_64
# platform naode:  Nilendras-MBP
# platform platform:  Darwin-22.1.0-x86_64-i386-64bit
# platform processor:  i386
# platform python build:  ('v3.7.4:e09359112e', 'Jul  8 2019 14:54:52')
# platform python compiler: Clang 6.0 (clang-600.0.57)
# platform python version: 3.7.4
# platform python implmentation: CPython
# platform release:  22.1.0
# platform system:  Darwin
# platform version:  Darwin Kernel Version 22.1.0: Sun Oct  9 20:14:54 PDT 2022; root:xnu-8792.41.9~2/RELEASE_X86_64
# uname:  uname_result(system='Darwin', node='Nilendras-MBP', release='22.1.0', version='Darwin Kernel Version 22.1.0: Sun Oct  9 20:14:54 PDT 2022; root:xnu-8792.41.9~2/RELEASE_X86_64', machine='x86_64', processor='i386')

# Process finished with exit code 0
