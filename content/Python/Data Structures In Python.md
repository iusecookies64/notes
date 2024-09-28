## Python Strings

In Python strings can be declared inside 
#### String Slicing
Slicing a string in python can be done as `string[startIndex : endIndex]` and this returns slice of string starting from given index up till (not including) the end index. If we want prefix of the string we can either give do `string[0 : endIndex]` or do `string[: endIndex]` similarly if we want to suffix we can give end index equal to length of string or simply omit it i.e. `string[startIndex:]`.
#### Steps in String Slicing
We can give an additional parameter which is the step size, this will give us string starting from start index and take jumps of given step size, the syntax is `string[startIndex:endIndex:stepSize]`. By default step size is `1`.
**Note:** If we give step size of $-1$ then it will take steps backwards, this is not useful if we are slicing partial string, but if we can use this to reverse the string i.e. `string[::-1]`.
**Note:** Slicing and indexing in pythons lists is same as strings.
#### Strings Are Immutable
Strings are immutable in python that means we cannot change a character in the string, for example we cannot do `strVariable[indx] = 'R'`. To reassign a character at some index in a string we need use string concatenation i.e. `newString = oldStr[:indx-1] + 'R' + oldStr[indx+1:]`.
#### String Multiplication
We can multiply a string with a number we get a bigger string in which original string is repeated number times. For example if `a = '1'` then `a * 10` returns `'11111'`.
#### String Methods
1. `str.capitalize()`: capitalizes `str` and returns it, does not affect `str`.
2. `str.upper/lower():` converts all characters to uppercase or lowercase and returns modified string.
3. `str.split()`: splits the string in words and returns the list of words. Splitting is based on some delimiter which by default is single space, and we can pass delimiter as argument also.
#### String Formatting
We can insert values into a string using string formatting, there are 2 ways to format strings.

1. First is using the format method as shown below,

```Python
name = 'Super'
print('His name is {} {}'.format(name, 'Man'))
# output = His name is Super Man

# using indexes of arguments
print('The {0} {0} {1}'.format('Fox', 'brown', 'quick'))
# output = The Fox Fox brown

#using named arguments
print('The {q} {b} {f}'.format(f = 'Fox', b = 'brown', q = 'quick'))
# output = The quick brown fox
```

2. The second method is using **f** strings as shown below

```python
fname = 'Super'
lname = 'Man'

print(f'His name is {fname} {lname}')
# output = His name is Super Man
```

**Note:** we can format floating point numbers using string formatting, inside the `{}` of a formatted string we can define the minimum width and the precision of the float number. The syntax is `value:width.precisionf`

```python
num = 123.456789

print(f'Formatted float is {num:2.3f}')
# output = Formatted float is 123.457
```

## Python Lists, Dictionaries, Tuples and More

### Lists in Python
Arrays in python are called lists, and we can store different data types in a single list unlike other programming languages (C++). To create a list we can simply do use square brackets as shown below.

```Python
new_list = [2, 'hello', 3]
```

A list literally have any other data type i.e. both primitive and not-primitive data types, that means list can have other lists inside and have dictionaries or any other data types in them.
#### List Methods
1. `list.append()`: this method adds the argument to the end of the list. This method modifies the original list.
2. `list.pop()`: this method removes the argument element from the list and returns it. If no argument is gives it by default removes the last element. This method is in-place that means it modifies the original list.
3. `list.sort():` this method sorts the list in place.
4. `list.reverse()`: this method reverses the list in place.
**Note:** the sort method only works if the list contains a single type of data i.e. if it contains different type of data this method will throw an error.

### Dictionaries in Python

Dictionaries in python are used to store key value pairs, here key can be any *immutable object* and values can any other data type (even other dictionaries). To declare a dictionary we use curly braces as shown below.

```python
# declaring a new dictionary
my_dict = {
	'key': 'value',
	'key2': ['value', 2]
}

# adding new key value pair via assignment operator
my_dict['key3'] = {
	'key4': 'another dictionary'
}

# dictionaries are mutable
my_dict['key'] = 'new value'
```

Dictionaries are similar to **unordered_map** in C++, they use hash tables to store the values. 

**Note:** dictionaries doesn't store the keys in order they are added to it, this is because hashing is used to decide the position of a key in dictionary and the order in which they are inserted is of no significance.
#### Dictionary Methods
1. `dict.keys()`: returns an iterable-object containing keys of the dictionary.
2. `dict.values()`: returns an iterable-object containing values of the dictionary.
3. `dict.items()`: returns an iterable-object containing tuple of `(key, value)` pairs.

**Note:** an iterable-object is like an immutable list on which we can iterate via a for loop but not have properties like indexing etc. which other lists have. For example look at the below code

```python
my_dict = {
	1: 'v1',
	2: 'v2',
	3: 'v3'
}

for key in my_dict.keys():
	print(key)
# output: 1 2 3
```

**Note:** to know whether a key is present in a dictionary or not we can have different ways,

1. Using `dict.keys()`:

```python
my_dict = {}

check_key = 'key'

if check_key in my_dict.keys():
	print('key is present')
else:
	print('key is not present')
```

2. Using `dict.get()` method:

```python
my_dict = {}

check_key = 'key'

if my_dict.get(check_key) == None:
	print('key not present')
else:
	print('key is present')
```

> [!Note]
> `None` is a special data type in python which simply means nothing, this usually used as a placeholder for variables whose value will be assigned in future. Functions that don't have any return value also return `None` by default.

#### Deleting a Key in Dictionary

To delete a key we have two methods that we can use, first is to use `del` keyword and other is to use `dict.pop()` method as shown below.

```python
my_dict = {'k1': 1, 'k2': 2, 'k3': 3}
del my_dict['k1']
print(my_dict.pop('k2'))
# output: 2
print(my_dict)
# output: {'k3': 3}
```
### Tuples in Python

Tuples are just like lists but the only difference is that they are immutable which means that we cannot reassign value at some index. They are created using parenthesis as shown below.

```python
my_tuple = (1, 2, 'hello', [3, 4], (5, 6))

print(my_typle[0])
# output: 1

my_tuple[0] = 2
# error

print(my_tuple[3][0])
# output: 3

my_typle[3][0] = 123

print(my_typle[3][0])
# output: 123

print(my_typle[4][0])
# output: 5

my_typle[4][0] = 123
# error since item at index 4 is a tuple itself
```

We can even create tuples from lists as shown below.

```python
my_list = [1, 2, 3, 4]

my_typle = tuple(my_list)

print(my_tuple)
# output: (1, 2, 3, 4)
```
#### Tuple Methods

1. `tup.count()`: returns the number of occurrence of the argument in the tuple
2. `tup.index()`: returns the first index of the argument in the tuple. **Note** that if the argument is not present in the tuple it will throw an error.

#### Tuple Unpacking

Often we want to extract values out of tuple and assign them to some variables. For this we can either declare variables and assign them values using indexing or we can use tuple unpacking as shown below.

```python
my_tup = ('Super', 45, 'M')
(name, age, gender) = my_tup
# we can also do it this way without the parenthesis
name, age, gender = my_tup

print(f'The name is {name} and age is {age} and gender is {gender}')
# output: The name is Super and age is 45 and gender is M

# iterating over list of tuples
users = [('super man', 45), ('iron man', 40), ('hulk', 42)]
for (name, age) in users:
	print(name, age)

# more useful when iterating over dictionaries
my_dict = {'k1': 1, 'k2': 2, 'k3': 3}
for (key, value) in my_dict.items():
	print(f'key is {key} and value is {value}')
```

> [!Note]
> The number of arguments in the left side of unpacking must be same as size of tuple or else we get error.

> [!Note]
> We can use unpacking in lists as well just like in case of tuples.

### Sets in Python

They are used to store unique values, they are similar to `unordered_set` in C++. We create a set using `set()` to which we can pass an optional argument which is a list and it automatically gives all unique elements in the list.

```python
my_list = [1, 1, 1, 2, 3, 4, 1, 2, 3, 4, 5]
my_set = set(my_list)
print(my_set)
# output: {1, 2, 3, 4}
```

**Note:** Just like dictionaries the value in set is not stored in sorted order, rather they are stored according to their hash value. For smaller values their hash value is gives their actual value but for very large values their hash is not equal to their value since in hashing modulus is used. Hence it might seem that it is storing values in sorted order for small numbers.

## I/O Files in Python

To read a file in python we use the inbuilt `open(filePath, mode)` function. The mode by default is `r` which means read only, other possible modes are listed below.
1. `r`: opens file in read only mode.
2. `w`: opens file in write only mode, this mode removes if file with name already exist and creates a new file.
3. `a`: opens file in append mode which allows us to add text to file without overwriting it.
4. `r+`: opens file in read and write mode.
5. `w+`: opens file in write and read mode (overwrites original file).

**Note:** after opening a file we must close, otherwise it will remain occupied while the program is running preventing other apps to use it, to close a file we can use `close` method, but a better way to deal with files is using the `with` statements as shown in below code.

**Note:** using reading data from file we start reading from where our cursor is currently at, initially the cursor is at the start of the file, and when we do operations like `read()` or `readlines()` that read the whole file the cursor moves to the end and further reading operations give nothing. To move the cursor at a particular position we use the `seek()` method as shown below.

```python
f = open('text.txt') # by default the mode is read only

content = f.read() # returns all full content of file in a single string
f.seek(0) # moving cursor back to start

lines_list = f.readlines()
f.seek(0)

# code to print each line using readline
line = f.readline()
while line:
	print(line)
	line = f.readline()

```

Opening files using `with` statement.

```python
with open('test.txt', mode='w') as f:
	f.write('overriting text in the file with this')
	f.write('file is closed as this block ends')
```

## Useful Functions in Python

### The `range()` Function

The `range()` function in python is used to iterate a for loop for certain amount of iterations, it returns an object of class range and we can use it as shown below. The function takes 3 arguments i.e. `range(start, end, step)` where start and step are optional. By default start is equal to `0` and step is `1`. 

```python
for i in range(10):
	print(i)

# output: 0 1 2 3 4 5 6 7 8 9
```

More specifically the range function is a **generator function**. We can use it to store a list of numbers which actually doesn't actually store the list, but rather the list on demand. We will learn more about generators in python later.
### The `enumerate()` Function

Often we need to loop over iterables like lists and strings. Using the `for item in items:` we can get the item but often along with the item we want the index of the item. For this people usually needed to maintain index variable themselves. To solve this problem python introduced enumerate function which can be used as shown.

```python
word = 'Super'

for item in enumerate(word):
	print(item)

# output
# (0, 'S')
# (1, 'u')
# (2, 'p')
# (3, 'e')
# (4, 'r')

# using tuple unpacking
for (index, value) in enumerate(word):
	print(index, value)

# output:
# 0 S
# 1 u
# 2 p
# 3 e
# 4 r
```

> [!Note]
> The `enumerate()` function also returns a generator which behaves like a list when we try to iterate over it. To actually convert a generator to a list we can use casting i.e. call `list()` and pass the generator as argument.

### The `zip()` Function

This function is used to zip together multiple lists and returns a generator of tuples. If makes tuples of corresponding elements in the lists. If the list are of different types then it only zips till the smallest list and then stops.

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['testing', 'the', 'zip', 'function']

for item in zip(list1, list2, list3):
	print(item)
# output:
# (1, 'a', 'testing')
# (2, 'b', 'the')
# (3, 'c', 'zip')
```

### The `in` Operator

When used inside of a for loop the `in` operator gets us the items of the iterable. When used inside a conditional statement, the `in` operator returns a Boolean telling whether a specified item is present in the iterable or not.

```python
word = 'Super Man'

# using in to iterate over string
for char in word:
	print(char)

# using in as conditional operator
if 'a' in word:
	print('a is present in the word')
```

### The `min` and `max` Functions

These are used to get the minimum and maximum value from an iterable value.

```python
word = 'super'
print(min(word))
print(max(word))
# output
# e
# s

print(min(range(10)))
print(max(range(10)))
# output
# 0
# 9
```

### The `random` Module

The `random` has many useful functions as shown below.

```python
import random

my_list = [1, 2, 3, 4, 5]
# shuffles the list in place
random.shuffle(my_list)
print(my_list)
# output: [3, 1, 5, 4, 2]

# getting a random integer in the given range
print(random.randint(1, 10))
# output: 7

# random.random() gives a random floating point in range 0 to 1
```

> [!Note]
> Similarly there is a `math` module which has many useful math functions

### The `input()` Function

This is used to take input from user from the command line. We can pass a string to show to user and give instructions about the input value.

```python
name = input('Enter your name: ')
age = input('Enter your age: ')
print(f'name is {name} and age is {age}`)
```

> [!Note]
> The `input` function always returns the input as a string, if we need it as any other data type we need to caste it to that data type. For example to take input a number we use `int(input())`.

### List Comprehension in Python

Often we find ourselves using loops to populate a list. In python there is a nice sleek way to achieve the same using list comprehension. Few common examples of list comprehension are shown below.

```python
# the normal ways to populate a list
nums = [1, 2, 3]
squared_nums = []
for num in nums:
	squared_nums.append(num ** 2)

# list comprehension to do the same thins in one line
squared_nums = [x ** 2 for x in nums]

# list comprehension with if statement
odd_nums = [num for num in range(10) if num%2 == 1]

# list comprehension with if/else statement
nums = [num if num%2 == 0 else -num for num in range(10)]
print(nums)
# output: [0, -1, 2, -3, 4, -5, 6, -7, 8, -9]

# nested loops list comprehension
my_list = [x * y for x in range(10) for y in range(10)]
```

> [!Note]
> Although list comprehension reduces the lines of code that we need to write, but it makes the code less readable, specially if we write really complicated comprehension. Always prefer code readability over the amount of code that you write.

