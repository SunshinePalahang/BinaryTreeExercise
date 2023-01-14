class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return

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

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # # find min element in the tree 
    # def find_min(self):
    #     if self.left is None:
    #         return self.data
    #     return self.left.find_min()
    # # find max element in the tree
    # def find_max(self):
    #     if self.right is None:
    #         return self.data
    #     return self.right.find_max() 
    # # find the sum of all elements 
    # def find_sum(self):
    #     left = self.left.find_sum() if self.left else 0
    #     right = self.right.find_sum() if self.right else 0
    #     return self.data + left + right
    # perform in post order traversal
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        return elements
    # perform in pre order traversal
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__=='__main__':
    letters = ['S', 'U', 'N', 'S', 'H', 'I', 'N', 'E', 'R', 'I', 'C', 'H', 'M', 'E', 'R', 'P', 'A', 'L', 'A', 'H', 'A', 'N', 'G']
    letters_tree = build_tree(letters)

    # print("Minimum Number is: ", letters_tree.find_min())
    # print("Maximum Number is: ", letters_tree.find_max())
    # print("Sum is: ", letters_tree.find_sum())
    print("In Order Traversal: ", letters_tree.in_order_traversal())
    print("Post Order Traversal: ", letters_tree.post_order_traversal())
    print("Pre Order Traversal: ", letters_tree.pre_order_traversal())

 
