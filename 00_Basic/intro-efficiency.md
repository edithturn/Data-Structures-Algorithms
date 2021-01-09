# Efficiency

Efficiency, also call Complexity.

It is how well we using our computer's resources to get a particular job done.

Space
- How long does your code take to run
Time
- How much storage space do you need?

Belong are some examples of fcuntions in Python. Note the time efficiency

```python
"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

def example1(manatees):
    for manatee in manatees:
        print manatee['name']
def example2(manatees):
    print (manatees[0]['name'])
    print (manatees[0]['age'])
def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print(manatee_property, ": " , manatee[mantee_property])
def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        if manatee1['age'] < manatee2['age']:
            oldest_manatee = manatee2p['name']
        else:
            oldest_manatee = manatee1['name']
    print(oldest_manatee)
```

