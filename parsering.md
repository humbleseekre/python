#from https://docs.python.org/3/library/argparse.html
#https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3

# The argparse module provides a more sophisticated mechanism to process command line arguments. 
# The following script extracts one or more filenames and an optional number of lines to be displayed:

import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

# When run at the command line with python top.py --lines=5 alpha.txt beta.txt, the script sets args.lines to 5 
# and args.filenames to ['alpha.txt', 'beta.txt'].

def sum(num1, num2):
    print("the sum of two nums is {}".format(num1 + num2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Add two numbers", prog='test.py')
    parser.add_argument('x', type=int)
    parser.add_argument('y',  type=int)
    args = parser.parse_args()
    sum(args.x, args.y)
    

#Above file usage:
#test.py 1 2
#the sum of two nums is 3
#(venv) (base) Nilendras-MBP:test_python neil$ python3 test.py -x 1 -y 2
#when:
 #   parser.add_argument('-x', type=int)
 #   parser.add_argument('-y',  type=int)
#usage: test.py [-h] -x -y
#(venv) (base) Nilendras-MBP:test_python neil$ python3 test.py -x 1 -y 2
#the sum of two nums is 3

In the Python `argparse` module, the `action` parameter in `add_argument()` **specifies what should be done when the argument is encountered on the command line**.

---

### 🔍 Your line:

```python
args.add_argument("--is_student", "-is", action="store_true", help="Is the primary user a student?")
```

### ✅ What `action="store_true"` does:

* It **stores `True`** if the flag (`--is_student` or `-is`) is **present** in the command line.
* It **stores `False`** if the flag is **not present**.

### Example:

```bash
python script.py --is_student
```

In your Python script:

```python
print(args.is_student)  # True
```

```bash
python script.py
```

```python
print(args.is_student)  # False
```

---

### 🧠 Why use it?

It’s useful for **boolean flags** where presence means **yes/true**, and absence means **no/false**—like `--verbose`, `--debug`, or `--is_student`.

Let me know if you want the equivalent for storing `False` (i.e. `store_false`).


