Decorators in Python are used to wrap functions around with other functionality. For example consider that we want to calculate the time that a function takes to execute, for this what we can do is write a function `time` which takes in a function as argument and returns another function. The returned the the original function with additional functionality that it prints the time it took to execute.

Look at the code to that implements the `time` function.

```python
import time

def time(func):
	# wrapper function will wrap given function
	# the argument that it takes must be or generic types because we don't know what type of arguments func takes
	def wrapper(*args, **kwargs):
		start = time.time()
		# actually executing the function
		result = func(*args, **kwargs) # wrapper knows func because of closures
		end = time.time()
		# printing time taken
		print(f'function {func.__name__} took {end - start} time')
		# returning result as normally func would
		return result

	# returning wrapper which wraps func
	return wrapper

def my_function(a, b):
	time.sleep(5)
	return a + b

modified_my_function = time(my_function)

print(my_function(1, 2)) # output 3

print(modified_my_function(1, 2))
# output
# function modified_my_function took 5.00120123 time
# 3
```

The issue with this approach is that it is ugly to do this for every function and we also have to change the name of the original function. The same functionality can be achieved by using python decorators, which are functions that take argument a function and return another function which wraps the argument function i.e. just like our `time` function.

Below is the code that achieves the same using decorators.

```python
# the code for time function will remain the same

@time
def my_function(a, b):
	time.sleep(5)
	return a + b

print(my_function(1, 2))
# output
# function modified_my_function took 5.00120123 time
# 3
```

As we can see that adding `@time` above our function definition converts the function `my_function` to modified function that is returned by `time` and we didn't even had to change the name of the function.

**Exercise:** To practice more about decorators write 2 more decorators, one is `logger` decorator which prints the function name along with the arguments with which it got called, and the other decorator we want is `cache` which caches arguments that a function receives and caches the return value. Then if the function gets called with the same set of arguments again, we simply return the cached value and not call the function.

**Solution:**

Solution for logger decorator.

```python
def logger(func):
	def wrapper(*args, **kwargs):
		print(f'{func.__name__} is called with args {args} and kwargs {kwargs})
		return func(*args, **kwargs)
	return wrapper

@logger
def add(a, b):
	return a + b

print(add(1, 2))
# output
# add is called with args (1, 2) and kwargs {}
# 3
```

Solution for `cache` decorator.

```python
def cache(func):
	cached_values = {}
	def wrapper(*args):
		# if args not in cached values, calculate result
		if args not in cached_values:
			cached_values[args]	= func(*args)
		return cached_values[args]

	return wrapper

@cache
def add(a, b):
	return a + b

print(add(1, 2))
print(add(1, 2))
# output
# 3
# 3
```