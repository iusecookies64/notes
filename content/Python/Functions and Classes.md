## Functions in Python

To declare function we need to use the `def` keyword followed by the function name and arguments signature and finally the block of code that needs to be run when this function is called. For example look at the code below.

```python
def my_function(argument1, argument2):
	print(f'my function called with arguments {argument1} and {argument2}')
	return argument1 + argument2

output = my_function(1, 2)
print(output)
# output
# my function called with arguments 1 and 2
# 3
```

To give default value to arguments we need to simply assign them default value in function declaration as shown below. Once a parameter is given default value, all parameters after this must also have a default value.

```python
def add_numbers(num1 = 0, num2 = 0):
	return num1 + num2

# below function will throw error
def add_numbers2(num1 = 0, num2):
	return num1 + num2

# this is valid
def add_numbers3(num1, num2 = 0):
	return num1 + num2
```

We can also call functions and pass arguments with by the variable names, as shown in the code below.

```python
def sample_function(arg1, arg2):
	print(arg1, arg2)

sample_function(arg1 = 1, arg2 = 2)
# output: 1 2

sample_function(arg2 = 2, arg1 = 1)
# output: 1 2
```

> [!Note]
> In python the naming convention is for functions we use snake casing i.e. `this_is_snake_case` and for classes we use capital casing i.e. `ThiIsCapitalCasing`.
> 

#### The `*args` and `**kwargs` in Python Functions
`*args` helps us take variable number of arguments for our function. In our function declarations we start with defining normal positional arguments and then followed by variable number of arguments, the order can never be other way around. Python knows that all arguments that don't have a named variable needs to go inside `*args` which is a tuple of all such values. This is shown in below code.

```python
def add_numbers(a, b, *args):
	print(args)
	sum = a + b
	for num in args:
		sum += num
	return sum

sum = add_numbers(1, 2, 3, 4)
print(sum)
# output
# (3, 4)
# 6
```

`**kwargs` helps us take keyword arguments as input to our functions. Keyword arguments are arguments that have names, we have already used this when we were learning about files I/O operations where we explicitly set the `mode` in which we want to open the file in. Below is a demonstrates the use of this keyword.

```python
def func(**kwargs):
	print(kwargs)

func(arg1='hello', arg2='kwargs')
# output: {'arg1': 'hello', 'arg2': 'kwargs'}
```

> [!Note]
> What makes these arguments special is not there name i.e. `args` and `kwargs` are just naming conventions and not part of the syntax to take argument, rather the thing that makes them special are `*` and `**` which means we can name them anything as long as we are using `*` and `**`.

The `*` and `**` are also used to spread iterables and dictionaries when passing them as arguments to functions. This is also helpful when we are taking input for a function as `*args` and `**kwargs` and we want to pass these to other functions in similar way. For example look at the code below.

```python
def func(name, age):
	print(name, age)

user_details = {
	"name": "Super Man",
	"age": 45
}
# spreading dictionary
func(**user_details) # output: Super Man 45

def func(*args):
	print(*args)

nums = [1, 2, 3]

func(*nums) # output: 1 2 3
```

## Map, Filter and Lambda Expressions

#### The `map()` Function
If we want to apply some function for every argument of an iterable in python we can either do a for loop and store the result in a new list or we can use the `map` function. The first argument is a function and the second argument is the iterable. It returns an iterable which has the modified values, this is similar to map function in JavaScript.

```python
def square(num):
	return num ** 2
	
nums = [1, 2, 3, 4]

for num in map(square, nums):
	print(num)
# output: 1 4 9 16

squared_nums = list(map(square, nums))

print(squared_nums)
# output: [1, 4, 9, 16]
```

#### The `filter()` Function
The filter function is used to filter out values from an iterable, it accepts a function and an iterable, then it runs the function for each item in the iterable and returns an iterable with those values for whom the function returned with `True`.

```python
def even_check(num):
	return num%2 == 0

my_nums = [1, 2, 3, 4, 5]

my_even_nums = filter(even_check, my_nums)

print(list(my_even_nums))
# output: [2, 4]
```

#### Lambda Expressions
These help use to write single line anonymous functions like functions shown above i.e. `even_check` or `square`. This is mostly useful to pass functions to functions like `map` and `filter` which are single use and we don't need them persistently. The syntax is `lambda argument: returnValue`.

```python
my_nums = [1, 2, 3, 4, 5]

my_squared_nums = map(lambda x:x**2, my_nums)
my_even_nums = filter(lambda x:x%2 == 0, my_nums)

print(list(my_squared_nums))
print(list(my_even_nums))
# output
# [1, 4, 9, 16, 25]
# [2, 4]
```

## Scope and LEGB Rule

#### Scope
Scope refers to the context in which a variable is accessible and writable i.e. in other words the region in which a variable is available. Scopes are created when we call functions and variables declared inside this scope gets lost once the function is ended. For example look at the code below.

```python
# this is global scope
x = 50
print('x in global scope is', x)
# output: x in global scope is 50

def func():
	// local function scope
	x = 100
	print('x in local scope is', x)
	y = 200


func()
# output: x in local scope is 100
print(y) # error since there is not y in this scope
```

This means if we declare a variable inside of a `for/while` loop then these variables will be available outside of the loops as well as long as we are in the current scope. For example look at the code below.

```python
def func():
	for x in range(10):
		pass
	# print x after loop has ended
	print(x) # outputs 9

func()
print(x) # x is not defined error
```
#### LEGB Rule
Python uses this rule to decide which variable to use. When we access a variable, python first looks for that variable in local scope (**L**), if it is not able to find it then it looks for that variable in enclosing functions local scope (E), if it doesn't find it there then it looks for in global scope (G). If python still couldn't find this variable, then it looks for it in the built-in functions (B).

```python
# global
x = 50
y = 51
z = 52

def func():
	# enclosing function's local
	x = 100
	y = 101
	
	def func2():
		# local
		x = 200
		print('local', x, y, z)

	func2()
	
	print('enclosing local', x, y, z)

func()

print('global', x, y, z)

# output
# local 200 101 52
# enclosing local 100 101 52
# global 50 51 52
```

#### The `global` and `nonlocal` Keywords
As we know that when accessing a variable as value inside a scope, we first look for that variable in current scope, then in outer scope and then its outer scope and so on. But when trying to assign value to a variable that is not present in the scope, python creates that variable. So there is no way to directly assign value to a variable in of outer scope inside inner scope. 

To tackle this problem we use the `global` and `nonlocal` keywords. Inside of our function scope if we want to access a variable of outside scope in both readable and writable mode we need to declare it as the start of the scope. If we use `nonlocal` then the search for that variable will be done from inner scope to outer scope. If we use `global` then we will be searching for this variable in global scope.

Below code demonstrates the usage of these keywords.

```python
# global x
x = 10

def func():
	x = 20 # local x
	
	def func2():
		nonlocal x
		x = 30
		print(x)
	
	def func3():
		global x
		x = 40
		print(x)
	
	func2() # outputs 30
	func3() # outputs 40

	print(x) # outputs 30 because func2 changed this

func()

print(x) # outputs 40 because func3 inside func updated this
```

> [!Note]
> The reason I came across these was because I was writing a function in which i was using a variable from outside and trying to increase its value by $1$ using `+=` operator. But I was getting error, since I was able to print the variable, I was confused by this behavior, which is I can read the variable but not modify it. For `+=` to work the variable must already be defined, and which in my case was not. It gave the error *UnboundLocalError: cannot access local variable 'x' where it is not associated with a value*
> 
#### Closures in Python
A *Closure* are functions with data attached to them. When a function is returned from a function or being passed to another function as argument, then what is being passed is actually closure which is the function along with an environment i.e. a mapping of variables that were used inside of the function but was declared in outside scope.

Look at the code below, the functions `inner` and `inner2` are using outer outer scope variable `x` and the function `func` returns these functions. Now when the call to `func` ends what normally happens that all variables are deleted. But since we have functions using these variables, the function are attached with these variables and then returned. This is what closure is, the functions `inner` and `inner2` are closures with access to variable `x`. Hence when these are called they don't throw any error and are able to use and modify these variables.

```python
def func():
    x = 10
    def inner():
        nonlocal x
        x += 1
        print(x)

    def inner2():
        nonlocal x
        x += 1
        print(x)

    return inner, inner2

inner, inner2 = func()

inner() # 11
inner2() # 12
inner() # 13
inner2() # 14
```

#### Memory Management in Python
When we create objects in python, the variables are just reference to those objects in memory. We can create multiple references to the same object by simply assigning them to another variable or passing them as arguments to functions.

When we delete a reference variable using the `del` keyword or the variable is deleted due to function scope ending, this doesn't necessarily mean that the object it refers to is also deleted. Python objects use reference counts for memory management. When a reference variable gets deleted the reference count of object decreases and when the reference count becomes `0` the object is eventually deleted from memory by python.

For example look at this code below.

```python
def func():
	print('func')

func2 = func

print(func2 == func) # true
# id prints address in memory, which is same for both of them
print(id(func))
print(id(func2))

del func # deleting one reference to function object

func2() # function still works, because it is still in memory
```
## Classes In Python

To define a class in python we use the class keyword followed by class name (which should be in capital casing by convention, but not compulsory). The name is followed by parenthesis inside which we may pass another class if this is an inherited class and finally the class block starts.

There is a special function called `__init__` which acts as a constructor for this class and is called whenever we create an instance of this class.

**Methods** in a class can be defined by simply writing functions inside the class block. When these methods are called by an instance of the class then by default the first argument is passed is the object itself (same as this in other languages) followed by other arguments.

```python
class Animal():
	# we can define other attributes that doesn't need initialization
	species = 'Mammal'
	
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# first argument is the object itself
	def print_details(self):
		print(self.name, self.age)

	# function to show difference between method and class function
	def print_args(arg1, arg2):
		print(type(arg1), type(arg2))

first_animal = Animal('Super', 45)
first_animal.print_details()
# output: Super 45

# we can only pass 1 argument, since first argument is always self
first_animal.print_args('hello')
# output: <class '__main__.Animal'> <class 'str'>

# we can also call it from animal class, but we need to pass 2 args this time
Animal.print_args(1, '1')
# output: <class 'int'> <class 'str'>

```

From above code we understand that functions inside a class can act as methods for class instances and they can also act as static functions of the class. If used as methods, first argument they receive is always the object calling the method.
#### Inheritance And Polymorphism
To inherit from a class we need to pass that class into our class, then inside constructor of this class we need to call constructor of inherited class as shown below. There are two ways to call constructor of parent class from inherited class as shown below, we must use only one of these.

```python
class Animal():
    def __init__(self, name):
        self.name = name  

    def speak(self):
        print(f"Hello, my name is {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # method 1
        Animal.__init__(self, name) # method 2
        self.breed = breed

    def bark(self):
        print('woof!')

obj = Dog('Buddy', 'Golden Retriever')
obj.speak()
obj.bark()
# output
# Hello, my name is Buddy
# woof!
```

> [!Note]
> If the derived class does not have any constructor, then the constructor of parent class is automatically called.

To achieve polymorphism in python classes, we can create a base class and define methods with body that throws an error, this way we cannot accidently create instance of the base class.

```python
class Animal():
	def __init__(self, name):
		self.name = name

	def introduce(self):
		print(f'hello, my name is {self.name}')

	def speak(self):
		raise NotImplementedError('This method must be called from derived class')

class Dog(Animal):
	def speak(self):
		print('Bark!')

class Cat(Animal):
	def speak(self):
		print('Meow!')

obj1 = Animal('mark')
obj2 = Dog('zuker')
obj3 = Cat('berg')

obj1.speak() # error
obj2.speak() # Bark!
obj3.speak() # Meow!
```

#### The Magic/Dunder Methods
In python we have ability to define what happens when objects from our custom classes are passed inbuilt functions like `print`, `len`, `del` etc. This is shown in the code below.

```python
from random import randint

class MyClass():
	def __init__(self, name):
		this.id = randint()
		this.name = name
	
	# function by print
	def __str__(self):
		return f'id is {self.id} and name is {self.name}'
	
	# function called by len
	def __len__(self):
		return len(self.name)
	
	# function called when we delete this object
	def __del__(self):
		print('Object is deleted')

class_object = MyClass('Super Man')
print(class_object) # output: id is 370 and name is Super Man
print(len(class_object)) # output: 9

del class_object # output: Object is deleted
```

