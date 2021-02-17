# Linked List
#Python does not have linked lists in its standard library. It is possible to  make classes that represent data structures in Python.


#The class "Element" will be a single unit in a linked list:
class Elemetn(Objetc):
    def __init__(self, value):
        self.value = value
        self.next = None # next is going to be the pointe to the next element in the linked list

#The class "LinkedList" will have a "head" 
class LinkesList(object):
    def __init__(self, head=None):
        self.head = head      # Creating the pointer to the first element of the array
# Funtion "append" will add a new node to the linked list
    def append(self, new_element):
# Create a new variable to storage the current head
        current = self.head
# If the head has a content, then we will iterate the list, until it doesn't have more elements
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else: # If there are not element in the linked list, the head will be asigned to a new element in the node
            self.head = new_element

