## Python Strings

In Python strings can be declared inside 
#### String Slicing
Slicing a string in python can be done as `string[startIndex : endIndex]` and this returns slice of string starting from given index up till (not including) the end index. If we want prefix of the string we can either give do `string[0 : endIndex]` or do `string[: endIndex]` similarly if we want to suffix we can give end index equal to length of string or simply omit it i.e `string[startIndex:]`.
#### Steps in String Slicing
We can give an additional parameter which is the step size, this will give us string starting from start index and take jumps of given step size, the syntax is `string[startIndex:endIndex:stepSize]`. By default step size is `1`.
**Note:** If we give step size of $-1$ then it will take steps backwards, this is not useful if we are slicing partial string, but if we can use this to reverse the string i.e `string[::-1]`.
**Note:** Slicing and indexing in pythons lists is same as strings.
#### Strings Are Immutable
Strings are immutable in python that means we cannot change a character in the string, for example we cannot do `strVariable[indx] = 'R'`. To reassign a character at some index in a string we need use string concatenation i.e `newString = oldStr[:indx-1] + 'R' + oldStr[indx+1:]`.
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

## Python Lists, Dictionaries and Tuples

### Lists