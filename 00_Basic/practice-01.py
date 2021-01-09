"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    # The constructor of the class
    def __init__(self):
    # Initializing the list called "items"
        self.items = []
    # Function to add an new item to the list
    def addItem(self, item):
    # Append will add a new element at the end of the list
        self.items.append(item)
    # Function to calculate what is the total score of the elements in my list
    def getClassiness(self):
    # Initializing variable to storate the partial sum
        _sum = 0
    # If my list has items, so we will iterate it
        if len(self.items) > 0:
    # Iterate all the elements in the list 
            for item in self.items:
    # If the element is "tophat"  it will be increase the value of 02 to the final sum "_sum"
                if item == "tophat":
                    _sum += 2
    # If the item is "bowtie" it will increate the value of 04 to the final sum "_sum"
                elif item == "bowtie":
                    _sum += 4
    # If the item is "monocle" it will increate the value of 05 to the final sum "_sum"
                elif item == "monocle":
                    _sum += 5
    # If the item doesn't exist in the list, will will add zero to the final sum "_sum"
                else:
                    _sum += 0
    # Returning teh final sum of all the elements in the list
        return _sum

# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

# Adding more elements
me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")

# Calling the function to know the total points
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())