#stack is last in first out function - LIFO
from collections import deque #importing the deque for stacjk implementation
#class for stack
class Stack:
    #init function to create a stack
    def __init__(self):
        self.container = deque()
    #push function to add values to the stack
    def push(self,val):
        self.container.append(val)
    #pop function to remove the last element in the stack
    def pop(self):
        return self.container.pop()
    #peek function to visit the last element in the stack
    def peek(self):
        return  self.container[-1]
    #function tu return true is the stack is empty
    def is_empty(self):
        return len(self.container)==0
    #function to return the size of the stack
    def size(self):
        return len(self.container)

#starting the main
if __name__ == "__main__":
    #creating the class object
    s = Stack()
    #pushing the values to the stack
    s.push(1)
    s.push(2)
    s.push(3)
    #printing the size of the stack
    print(s.size())
