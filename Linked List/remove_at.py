#Creating the class node
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
    function to remove at the given position
    first checcking the given index values
        if the index is less than 0 or greater than the length of the linked list raising exception
    if the index is 0 then the head is head.next to simply derefering the particular node the dereferenced node will be automatically freed

    else
        iterating through the linked list before to the given index
        then the address of itr is set as itr.next.next to dereference the next node of itr
        
    """
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    """
    function to insert the set of values in the linked list
    this function gets the list of values
    then iterate through the list values one by one
    then insering the value to the end by insert_at_end function
    """
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
            
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.remove_at(2)
    ll.print()
