# Functional programming
from flask import *
"""
Functional programming is progamming paradim where we mainly 
use immuatable function and avoid side effect.
It is usually used to write code with less or no bug  
"""

#Example 
"""Pure function"""
def add(a, b):
    return a + b

# This is a pure function as it only depends on its arguments
result = add(3, 5)
print(result)  # Output: 8

"""Immutability"""
# Immutable data types like tuples are preferred
original_tuple = (1, 2, 3)
new_tuple = original_tuple + (4,)
print(new_tuple)  # Output: (1, 2, 3, 4)

"""High order function"""
def apply_operation(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

result = apply_operation(add, 3, 5)
print(result)  # Output: 8

"""Recursion"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)  # Output: 120

"""Referential Transparency"""
# Instead of this
result = add(3, 5) + add(2, 4)

# You can replace expressions with their values
print(result)




