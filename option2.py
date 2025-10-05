# OPTION 2 - IMPLEMENT STACK
# DO NOT SHARE

# 2. Implement a growable integer stack (without using container libraries like vector, list, etc.)
#    that satisfies the following requirements:

# `push` adds a given value to the top
# `pop`  returns and removes the value at the top
# `peek` returns the value at the top
# `size` returns the count of values

# creating node class to hold values and next references
class Node:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class IntStack:
    
    def __init__(self):
        
        # dummy makes it cleaner to add nodes to head
        self.dummy = Node()
        self.stackSize = 0
    
    # method to add values to the top of the stack
    def push(self, val):

        # use .next to insert a new node
        newNode = Node(val, self.dummy.next)
        self.dummy.next = newNode
        self.stackSize += 1

    # method to remove the first element of the stack
    def pop(self):

        # stack can't be empty
        if self.stackSize == 0: 
            raise IndexError("Error, pop from empty stack.")

        # use .next to bypass the removed node
        removed = self.dummy.next
        self.dummy.next = removed.next
        self.stackSize -= 1
        return removed.val

    # method to return the top element of the stack
    def peek(self):

        # stack can't be empty
        if self.stackSize == 0: 
            raise IndexError("Error, peek from empty stack.")
        
        return self.dummy.next.val

    # method to return the size of the stack
    def size(self):
        return self.stackSize