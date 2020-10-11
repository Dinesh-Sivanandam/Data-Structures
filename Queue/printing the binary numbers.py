#importing the deque module from collections
from collections import deque

#creating the class for queue
class Queue:
    #constructor which automatically executes when the object is created
    #it creates the queue
    def __init__(self):
        self.buffer = deque()
    
    #function for enqueue
    #it adds the value to the left of the queue
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    #function for dequeue
    #it removes or pops the last element that is forst entered element to the queue and returns it    
    def dequeue(self):
        return self.buffer.pop()
    
    #function to check the queue is empty
    #if the self.buffer is empty it returns true
    def is_empty(self):
        return len(self.buffer)==0
    
    #function to return the size if the queue by the len method
    def size(self):
        return len(self.buffer)
    
    #function for returning the front element
    def front(self):
        return self.buffer[-1]

#function for producing the binary values
def produce_binary_numbers(n):
    #creating the queue for storing values
    if n == 0:
        print("0")
    numbers_queue = Queue()
    #appending '1' by enqueue method
    numbers_queue.enqueue("1")

    #iterating till the size reached
    for i in range(n):
        #getting the front value of the queue
        front = numbers_queue.front()
        #printing the front value
        print("   ", front)
        #after printing appending the values +0 and +1 in the queue
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        #removing the printed element from the queue
        numbers_queue.dequeue()

#starting the main
if __name__ == '__main__':
    #generating the binary numbers for specified value
    produce_binary_numbers(5)