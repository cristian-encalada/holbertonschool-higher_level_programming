# Python - More Classes and Objects

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
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using `wc`

## Mandatory Tasks

### 0. Simple rectangle

Write an empty class `Rectangle` that defines a rectangle:

- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/$ 
```
__No test cases needed__

File: [0-rectangle.py](./0-rectangle.py)

### 1. Real definition of a rectangle 

Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)

- Private instance attribute: `width`:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
        - `width` must be an integer, otherwise raise a TypeEr`ror exception with the message `width must be an integer`
        - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
        - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
        - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
guillaume@ubuntu:~/$ 
```
File: [1-rectangle.py](./1-rectangle.py)

### 2. Area and Perimeter

Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)

- Private instance attribute: `width`:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
        - `width` must be an integer, otherwise raise a TypeEr`ror exception with the message `width must be an integer`
        - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
        - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
        - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/$ 
```
File: [2-rectangle.py](./2-rectangle.py)

### 3. String representation

Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)

- Private instance attribute: `width`:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
        - `width` must be an integer, otherwise raise a TypeEr`ror exception with the message `width must be an integer`
        - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
        - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
        - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
    - if width or height is equal to 0, return an empty string
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
guillaume@ubuntu:~/$ 
```

File: [3-rectangle.py](./3-rectangle.py)

### 4. Eval is magic

Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)

- Private instance attribute: `width`:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
        - `width` must be an integer, otherwise raise a TypeEr`ror exception with the message `width must be an integer`
        - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
        - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
        - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
    - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

guillaume@ubuntu:~/$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/$ 
```
File: [4-rectangle.py](./4-rectangle.py)

### 5. Detect instance deletion 

Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)

- Private instance attribute: `width`:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
        - `width` must be an integer, otherwise raise a TypeEr`ror exception with the message `width must be an integer`
        - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
        - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
        - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
    - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is `deleted`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
guillaume@ubuntu:~/$ 
```
File: [5-rectangle.py](./5-rectangle.py)

### 6. How many instances 

Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)

- Private instance attribute: `width`:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
        - `width` must be an integer, otherwise raise a TypeEr`ror exception with the message `width must be an integer`
        - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
        - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
        - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
    - Initialized to `0`
    - Incremented during each new instance instantiation
    - Decremented during each instance deletion
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
    - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is `deleted`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

guillaume@ubuntu:~/$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/$ 
```

File: [6-rectangle.py](./6-rectangle.py)

###  7. Change representation

Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)

- Private instance attribute: `width`:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
        - `width` must be an integer, otherwise raise a TypeEr`ror exception with the message `width must be an integer`
        - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
        - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
        - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
    - Initialized to `0`
    - Incremented during each new instance instantiation
    - Decremented during each instance deletion
- Public class attribute `print_symbol`:
    - Initialized to `#`
    - Used as symbol for string representation
    - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
    - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is `deleted`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

guillaume@ubuntu:~/$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/$ 
```

File: [7-rectangle.py](./7-rectangle.py)

### 8. Compare rectangles

Write a class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)

- Private instance attribute: `width`:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
        - `width` must be an integer, otherwise raise a TypeEr`ror exception with the message `width must be an integer`
        - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
        - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
        - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
    - Initialized to `0`
    - Incremented during each new instance instantiation
    - Decremented during each instance deletion
- Public class attribute `print_symbol`:
    - Initialized to `#`
    - Used as symbol for string representation
    - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
    - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is `deleted`
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
    - `rect_1` must be an instance of Rectangle, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
    - `rect_2` must be an instance of Rectangle, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
    - Returns `rect_1` if both have the same area value
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

guillaume@ubuntu:~/$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/$ 
```
File: [/8-rectangle.py](./8-rectangle.py)

### 9. A square is a rectangle

Write a class `Rectangle` that defines a rectangle by: (based on `8-rectangle.py`)

- Private instance attribute: `width`:
    - property `def width(self):` to retrieve it
    - property setter `def width(self, value):` to set it:
        - `width` must be an integer, otherwise raise a TypeEr`ror exception with the message `width must be an integer`
        - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
    - property `def height(self):` to retrieve it
    - property setter `def height(self, value):` to set it:
        - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
        - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
    - Initialized to `0`
    - Incremented during each new instance instantiation
    - Decremented during each instance deletion
- Public class attribute `print_symbol`:
    - Initialized to `#`
    - Used as symbol for string representation
    - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
    - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
    - if width or height is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- Print the message `Bye rectangle...` (... being 3 dots not ellipsis) when an instance of `Rectangle` is `deleted`
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
    - `rect_1` must be an instance of Rectangle, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
    - `rect_2` must be an instance of Rectangle, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
    - Returns `rect_1` if both have the same area value
- Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

guillaume@ubuntu:~/$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/$ 
```
File: [9-rectangle.py](./9-rectangle.py)

## Advanced Tasks

### 10. Class and instance attributes 

Write a blog post describing how object and class attributes work.

- What’s a class attribute
- What’s an instance attribute
- What are all the ways to create them and what is the Pythonic way of doing it
- What are the differences between class and instance attributes
- What are the advantages and drawbacks of each of them
- How does Python deal with the object and class attributes using the `__dict__`

Your posts should have examples and at least one picture, at the top. Publish your blog post on Medium or LinkedIn, and share it at least on LinkedIn.

When done, please add all urls below (blog post, LinkedIn post, etc.)

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

### 11. N queens 

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

- Usage: `nqueens N`
    - If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status 1
- where N must be an integer greater or equal to 4
    - If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
    - If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
- The program should print every possible solution to the problem
    - One solution per line
    - Format: see example
    - You don’t have to print the solutions in a specific order
- You are only allowed to import the sys module

Read: [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

```python
julien@ubuntu:~/N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/N Queens$ 
```
File: [101-nqueens.py](./101-nqueens.py)


## Author

* __Cristian Encalada__ - *Holberton Student* 
    - Github: [Cristian Encalada](https://github.com/cristian-encalada/)