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
    Function for getting the length of the linked list
    initializes count = 0
    iterating the values of the linked list for each iteration incrementing the count
    once the last item reached returning the count value
    """
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        print (count)

if __name__ == "__main__":
    
    ll = LinkedList()
    ll.get_length()