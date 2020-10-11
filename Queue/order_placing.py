#importing threading and time
import threading
import time
#importing dequeue from collections
from collections import deque

#defining a queue
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
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    #function to check the queue is empty
    #if the self.buffer is empty it returns true
    def is_empty(self):
        return len(self.buffer) == 0

    #function to return the size if the queue by the len method
    def size(self):
        return len(self.buffer)

#creating the queue object
#when the object is created the queue is also created by the constructor
food_order_queue = Queue()

"""
function for placing the order
taking a order one by one and printing the order name
then appending the order to the queue by enqueue function
then we freese the program for 0.5s
"""
def place_orders(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)

"""
function for serving the orders
after placing there is a time to stop one second for preparing
then removing the first entered element and serving the value
then we wait for 2 seconds for next serving
"""
def serve_orders():
    time.sleep(1)
    while True:
        order = food_order_queue.dequeue()
        print("Now serving: ",order)
        time.sleep(2)

#starting the main function
if __name__ == '__main__':
    #creating the orders list
    orders = ['pizza','samosa','pasta','biryani','burger']
    #creating the threading objects
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    #starting the threads
    t1.start()
    t2.start()