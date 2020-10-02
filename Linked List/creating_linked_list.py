class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
#Creating the class for linked list
class LinkedList:
    #this statement initializes when created
    #initializing head is none at initial
    def __init__(self):
        self.head = None

if __name__ == "__main__":
    
    ll = LinkedList()