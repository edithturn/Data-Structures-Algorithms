# 01. Find the sum of all elements in a linked list, recursively.
# 02. Appended an element to the end of a linked list, recursively
# 03. Sum all numbers from 1 to n, where n is a positive number (similar to fibonacci)
# 04. Find the sum of all elements in an array with no for or while loop.
# 05. Recursive binary search


class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, val=0, next=None):
        self.head = None
 
    def sum_all_elements(self, head):
        if head:
           return head.data + self.sum_all_elements(head.next)
        return 0

    def append_end_list(self, head, data):
        if head == None:
            return Node(data)           
        else:
            head.next = self.append_end_list(head.next, data)            
        return head

    def print_list(self):
        llist = self.head
        while llist:
            print(llist.data)
            llist =llist.next


# Test Cases
# Linked List: 3 -> 4 -> 1 -> 2

# Crating Nodes

llist = LinkedList()
node1 = Node(3)
node2 = Node(4)
node3 = Node(1)
node4 = Node(2)

llist.head = node1

node1.next = node2
node2.next = node3
node3.next = node4


# Printing
llist.print_list()

# 01. Sum all elements in the LL
sumll = LinkedList()
print("The Sum of the element of the Linked List is: " + str(llist.sum_all_elements(llist.head)))
 
# 02. Append and element at the end ot the list
llist.append_end_list(llist.head, 8)

# Printing
print("After Append an element")
llist.print_list()

# 03. 