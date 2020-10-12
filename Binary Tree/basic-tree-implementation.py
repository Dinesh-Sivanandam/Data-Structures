#class for binary tree
class TreeNode:
    #constructor which initializes data, parent and children for a node
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    #function or method for getting the levels
    """
        setting the level to 0
        then assaigning p as self.parent
        going to the parents one by one by loop adn incremented as p.parent
            also incrementing the level value
        then returning the value
    """
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    #function to print the tree by hirerachy
    """
        assaigning spaces by level
            assaigning the spaces as 3 times the level of spaces to show its hirerachy
            then also add some characters only if self.parent is true else only spaces for neetness
        then printing the prefix and also data of node

        then we use recursion function to print all the node else we miss out the nodes after level 1
    """
    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    #function for adding the node in tree
    #initializing the parent to self
    #then appending the child to the self.children
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    #building the class object as root
    root = TreeNode("Electronics")
    
    #building object as with nodes and appending the child nodes to it
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    
    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    #adding the parent nodes to the root node
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    #then we print the tree
    root.print_tree()

#initializing the main class
if __name__ == '__main__':
    #calling the function
    build_product_tree()
