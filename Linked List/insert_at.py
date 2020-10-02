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
        
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    """
    function to insert the value at the given position
        first checcking the given index values
        if the index is less than 0 or greater than the length of the linked list raising exception

    if the index is 0 then we use insert_at_begining function to insert at the beginning

    else
        iterating through the linked list before to the given index
        creating the node by using the data and the address of the itr next
        placing the node after the node by itr.next
    """
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1
    
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

        return count
    
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
    ll.insert_at(0, "Jackfruit")
    ll.print()