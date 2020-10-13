class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def min_value(self):
        if self.left is None:
            return self.data
        return self.left.min_value()
    
    def max_value(self):
        if self.right is None:
            return self.data
        return self.right.max_value()
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    value = numbers_tree.in_order_traversal()
    min = numbers_tree.min_value()
    max = numbers_tree.max_value()
    print(min,max)