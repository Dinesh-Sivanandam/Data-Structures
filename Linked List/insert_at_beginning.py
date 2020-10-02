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
        
    """
    function for inserting the values at the head position
    creating a node by node class and setting the values
    then setting the node as head to insert at the begining
    """  
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    """
    Function for printing the linked list
    if the head is none the link list is empty
    else
    initializing the itr value as head and incrementing
    iterating until the itr is none and printing the values
    """
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

if __name__ == "__main__":
    
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at_begining("Jackfruti")
    ll.print()