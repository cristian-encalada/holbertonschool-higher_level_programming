# Python - Classes and Objects

## Table of contents
   1. [Requirements](#requirements)
   2. [Mandatory Tasks](#mandatory-tasks)
   3. [Advanced Tasks](#advanced-tasks)
   4. [Author](#author)

## Requirements

### Python scripts

* Allowed editors: ``vi``, ``vim``, ``emacs``
* All - - your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (version 3.8.*)
* All - - your files should end with a new line
* The first line of all - - your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of this project, is mandatory
* - - Your code should use the pycodestyle (`version 2.7.*`)
* All your files must be executable
* The length of your files will be tested using `wc`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation
    - `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
    -  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

__Documentation is now mandatory!__ Each module, class, and method must contain docstring as comments.
- Example: [Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

## Mandatory Tasks

### 0. My first square

Write an empty class `Square` that defines a square:

- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/$ 
```
File: [0-square.py](./0-square.py)

### 1. Square with size 

Write a class `Square` that defines a square by: (based on `0-square.py`)

- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/$ 
```
File: [1-square.py](./1-square.py)

### 2. Size validation

Write a class `Square` that defines a square by: (based on `1-square.py`)

- Private instance attribute: `size`
- Instantiation with optional `size: def __init__(self, size=0):`
    - size must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/$  
```
File: [2-square.py](./2-square.py)

### 3. Area of a square 

Write a class `Square` that defines a square by: (based on `2-square.py`)

- Private instance attribute: `size`
- Instantiation with optional `size: def __init__(self, size=0):`
    - size must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/$ 
```

File: [3-square.py](./3-square.py)

### 4. Access and update private attribute 

Write a class `Square` that defines a square by: (based on `3-square.py`)

- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size: def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/$ 
```
File: [4-square.py](./4-square.py)

### 5. Printing a square 

Write a class `Square` that defines a square by: (based on `4-square.py`)

- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size: def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character #:
    - if size is equal to 0, print an empty line
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/$ 
```
File: [5-square.py](./5-square.py)

### 6. Coordinates of a square 

Write a class `Square` that defines a square by: (based on `5-square.py`)

- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position`:
    - property `def position(self):` to retrieve it
    - property setter `def position(self, value):` to set it:
        - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional `size: def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character #:
    - if size is equal to 0, print an empty line
    - `position` should be use by using space - __Don’t fill lines by spaces__ when `position[1] > 0`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/$ 
```

File: [6-square.py](./6-square.py)

## Advanced Tasks

###  7. Singly linked list 

Write a class `Node` that defines a node of a singly linked list by:

- Private instance attribute: `data`:
    - property `def data(self):` to retrieve it
    - property setter `def data(self, value):` to set it:
        - `data` must be an integer, otherwise raise a `TypeError` exception with the message `data must be an integer`
- Private instance attribute: `next_node`:
    - property `def next_node(self):` to retrieve it
    - property setter `def next_node(self, value)`: to set it:
        - `next_node` can be `None` or must be a Node, otherwise raise a `TypeError` exception with the message `next_node must be a Node object`
- Instantiation with `data` and `next_node: def __init__(self, data, next_node=None):`

And, write a class `SinglyLinkedList` that defines a singly linked list by:

- Private instance attribute: `head` (no setter or getter)
- Simple instantiation: `def __init__(self):`
- Should be printable:
    - print the entire list in stdout
    - one node number by line
- Public instance method: `def sorted_insert(self, value):` that inserts a new `Node` into the correct sorted position in the list (increasing order)
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 100-main.py
#!/usr/bin/python3
SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

guillaume@ubuntu:~/$ ./100-main.py
-4
-3
1
2
3
3
4
5
5
10
12
guillaume@ubuntu:~/$ 
```

File: [100-singly_linked_list.py](./100-singly_linked_list.py)

### 8. Print Square instance  

Write a class `Square` that defines a square by: (based on `6-square.py`)

- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position`:
    - property `def position(self):` to retrieve it
    - property setter `def position(self, value):` to set it:
        - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional `size: def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character #:
    - if size is equal to 0, print an empty line
    - `position` should be use by using space
- Printing a `Square` instance should have the same behavior as my_print()
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 101-main.py
#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

guillaume@ubuntu:~/$ ./101-main.py | tr " " "_" | cat -e
#####$
#####$
#####$
#####$
#####$
--$
$
____#####$
____#####$
____#####$
____#####$
____#####$
guillaume@ubuntu:~/$ 
```
File: [101-square.py](./101-square.py)

### 9. Compare 2 squares 

Write a class `Square` that defines a square by: (based on 4-square.py)

- Private instance attribute: `size`:
    - property `def size(self):` to retrieve it
    - property setter `def size(self, value):` to set it:
        - `size` must be a number (float or integer), otherwise raise a `TypeError` exception with the message `size must be a number`
        - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with `size: def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- `Square` instance can answer to comparators: `==`, `!=`, `>`, `>=`, `<` and `<=` based on the square area
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 102-main.py
#!/usr/bin/python3
Square = __import__('102-square').Square

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")

guillaume@ubuntu:~/$ ./102-main.py
Square 5 < Square 6
Square 5 <= Square 6
Square 5 != Square 6
guillaume@ubuntu:~/$ 
```
File: [102-square.py](./102-square.py)

## Author

* __Cristian Encalada__ - *Holberton Student* 
    - Github: [Cristian Encalada](https://github.com/cristian-encalada/)