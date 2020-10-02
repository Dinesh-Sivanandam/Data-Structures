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
    function to insert values at the end of the linked list
    if the head is none then inserting the data in head
    else iterating through the values and reaching the last node
    then creating the node and placing the value and next is none
    and setting the irt next to the node
    """
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
        
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
    ll.insert_at_end("Jackfruti")
    ll.print()