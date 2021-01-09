# Remember the Basics of Python

## Comments

```python
#  This is aone-line Python comment.
""" This kind of comment is used to document the funciton and clases, usually multiple lines"""
```

## Declaration and Initialization

```python
# Variables, they have data types, a variable can be reassigned to contain a different data type

answer = 42
answer = "The answer is 42."
```

## Data Types
```python
boolean = true
number = 2.0
string = "This is a string"
list = ["First element", 2, 3, 4, "More elements"]
tuple = ("Tuples", "Can", "Have", "More Than", 2 , "Elements")
dictionary = {'one': 1, 'two': 2, 'three': 3}
varaible_with_zero_data = None
```

## Simple Logging
```python
print ("I am inside the function!")
```

## Conditional
```python
if cake == "delicious":
    return "Yes, I wish eat one!"
elif cake == "Okay":
    return "I'll have a small piece"
else:
    return "No, thank you"
```

## Loops
```python
for item in list:
    print item

while (total < max_val):
    total += values[i]
    i += 2
```

## Functions
```python
def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend /% divisor
    return quotient, remainder

def calculate-studd(x, y):
    (q, r) = divide(x, y)
    print (q, r)
```

## Clases
```python
class Person(Object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

```


Source: Data Structures $ Algorithms in Python