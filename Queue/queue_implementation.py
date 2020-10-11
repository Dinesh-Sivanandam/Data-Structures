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

#starting the main
if __name__ == "__main__":
    
    #creating the queue object
    pq = Queue()
    
    #initializing the values
    pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
    })
    pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })
    pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })

    #calling the dequeue function and printing the prices
    result = pq.dequeue()
    print(result['price'])
