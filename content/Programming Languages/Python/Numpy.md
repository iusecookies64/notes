### Why use Numpy

What makes NumPy so powerful that is either difficult or inefficient with standard lists or arrays?

**Performance and Efficiency**

- Faster Computations: NumPy arrays (ndarrays) are implemented in C and use contiguous memory allocation, which leads to faster operations compared to Python lists.
- Memory Efficiency: NumPy arrays use less memory than Python lists because they store elements of the same data type and have a more compact memory layout.

### Task

We have populated a simple code in the IDE that highlights the advantages of NumPy over Python lists for numerical computations is the calculation of the mean (average) of a large dataset.  
Run the code in the IDE and notice the following!

- Time taken using the List method is significantly higher versus time taken using the NumPy method

**Note:** Do not worry about the syntax, we will learn this in the subsequent modules.

```python
import random
import time
import numpy as np

# Method 1: Using Lists
# Generate a large list of random numbers
data_list = [random.random() for _ in range(1000000)]

# Calculate the mean using Python lists
start = time.time()
mean_list = sum(data_list) / len(data_list)
end = time.time()
print("Mean (list):", mean_list)
print("Time taken (list):", end - start)

# Method 2: Using NumPy
# Generate a large NumPy array of random numbers
data_array = np.random.random(1000000)

# Calculate the mean using NumPy
start = time.time()
mean_array = np.mean(data_array)
end = time.time()
print("Mean (NumPy):", mean_array)
print("Time taken (NumPy):", end - start)
```

### Why use Numpy

What makes NumPy so powerful? ... continued.

**Mathematical and Statistical Functions**

- Built-in Mathematical Functions: NumPy provides a wide range of mathematical functions for operations such as trigonometric functions, logarithms, and exponentials.
- Statistical Functions: Functions like mean, median, standard deviation, variance, etc., are available out-of-the-box for efficient computation.

### Task

We have populated a simple code in the IDE to compute the mean and standard deviation with and without NumPy.  
Run the code in the IDE and notice the following!

- The inbuilt statistical functions such as `mean` and `std` make the code a lot easier.

**Note:** Do not worry about the syntax, we will learn this in the subsequent modules.

```python
import math
import random
import numpy as np

# Method 1: Using regular Python
# Generate a large list of random numbers
data_list = [random.random() for _ in range(1000)]

# Calculate the mean and standard deviation
mean_list = sum(data_list) / len(data_list)
variance_list = sum((x - mean_list) ** 2 for x in data_list) / len(data_list)
std_dev_list = math.sqrt(variance_list)
print("Mean (list):", mean_list)
print("Standard Deviation (list):", std_dev_list)

# Method 2: Using NumPy
# Generate a large NumPy array of random numbers
data_array = np.random.random(1000)

# Calculate the mean
mean_array = np.mean(data_array)
std_dev_array = np.std(data_array)
print("Mean (NumPy):", mean_array)
print("Standard Deviation (NumPy):", std_dev_array)
```

### Why use Numpy

What makes NumPy so powerful? ... continued.

**Array Manipulation and Operations**

- Reshaping Arrays: NumPy allows you to easily reshape arrays, perform transpositions, and manage multidimensional data.
- Broadcasting: NumPy supports broadcasting, which allows operations on arrays of different shapes in a way that is both intuitive and efficient.

### Task

We have populated a simple code in the IDE to reshape arrays and perform array operations with and without NumPy.  
Run the code in the IDE and notice the following!

- In Python lists, we need to use nested loops to achieve the same results, which can be cumbersome and less efficient.

**Note:** Do not worry about the syntax, we will learn this in the subsequent modules.

```python
import numpy as np

# Method 1: Using Python Lists
# Create a 1D list
data_list = [1, 2, 3, 4, 5, 6]

# Reshape into a 2x3 "matrix"
data_matrix = [data_list[i:i + 3] for i in range(0, len(data_list), 3)]
print("Reshaped list (2x3):")
print(data_matrix)

# Transpose the "matrix"
transposed_matrix = [[data_matrix[j][i] for j in range(len(data_matrix))] for i in range(len(data_matrix[0]))]
print("Transposed list (3x2):")
print(transposed_matrix)

# Method 2: Using NumPy
# Create a 1D NumPy array
data_array = np.array([1, 2, 3, 4, 5, 6])

# Reshape into a 2x3 matrix
reshaped_array = data_array.reshape((2, 3))
print("Reshaped array (2x3):")
print(reshaped_array)

# Transpose the matrix
transposed_array = reshaped_array.T
print("Transposed array (3x2):")
print(transposed_array)
```

### Start with NumPy

Alright - lets begin our journey with NumPy.

NumPy (short for "Numerical Python") is a library for the Python programming language. We import NumPy in Python using the import statement.

```python
import numpy as np
```

- The code above imports the NumPy library with an alias `np`
- If we don't import - then every NumPy functional call needs to have the term `numpy`

### Task

Check the code given in the IDE to understand the usage of the alias `np`.  
Click on 'Submit' to view the result.

```python
import numpy as np

# Create a 1D NumPy array
data_array = np.array([1, 2, 3, 4, 5, 6])

print(data_array)
```

### NumPy array using randint

In the previous concept - we learnt to create a Numpy array using a Python list.  
We can also create a NumPy array containing 'n' random integers using the np.random.randint function.

```python
# Create a 1D array of 5 random integers between 0 and 10
random_array = np.random.randint(0, 10, size=5)
```

`np.random.randint(low, high, size)`: Generates random integers from low (inclusive) to high (exclusive).

- low: The lowest integer to be drawn from the distribution (inclusive).
- high: The highest integer to be drawn from the distribution (exclusive).
- size: The shape of the output array. In this case, size=5 means a 1D array with 5 elements.

Note that the following syntax creates an array of 5 random numbers - not necessarily integers

```python
array1 = np.random.rand(5)
```

### Task

Click on submit to see the output of the code given in the IDE. You can make changes to the 1D array code to understand how the implementation works.

```python
import numpy as np

# generate an array of 5 random numbers
array1 = np.random.rand(5)
print(array1)

# generate an array of 5 random integers between 0 and 10
random_array = np.random.randint(0, 10, size=5)
print(random_array)

```

### NumPy empty array

We can create an empty NumPy array using the `empty()` function.

```python
num = np.empty(5)
```

The above code creates an empty array of length 5.

Similar functions are the `zeros()` and `ones()` functions

```python
num0 = np.zeros(4)

num1 = np.ones(3)
```

num0 will have 4 elements all initialised to 0. num1 will have 3 elements all initialised to 1.

### Task

Check the code given in the IDE.  
Note that using the `empty()` function generates values in the array that are not set to any particular value but are just whatever values were already present in the allocated memory.

```python
import numpy as np

# create an array with 4 elements filled with zeros
num0 = np.zeros(4)

# create an array with 3 elements filled with ones
num1 = np.ones(4)

# create an empty array of length 5
num = np.empty(4)

print(num0)
print(num1)
print(num)
```
