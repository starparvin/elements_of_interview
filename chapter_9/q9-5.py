class Node(object):
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

    def add_right(self,node):
        # assert(isinstance(node,Node))
        self.right = Node(node)
        self.right.parent = self
        return self.right

    def add_left(self, node):
        # assert (isinstance(node, Node))
        self.left = Node(node)
        self.left.parent = self
        return self.left

    def is_left_child(self):
        return self.parent.left == self
    # def has_left(self):
    #     return self.left
    #
    # def has_right(self):
    #     return self.right

def inorder_iterative(root):
    assert (isinstance(root, Node))
    if not root:
        return
    curr_node = root
    prev_node = None
    next_node = None
    list_inorder = []

    while curr_node:
        if not prev_node or prev_node.left == curr_node or prev_node.right == curr_node:
            if curr_node.left:
                next_node = curr_node.left
            else:
                list_inorder.append(curr_node.data)
                if curr_node.right:
                    next_node = curr_node.right
                else:
                    next_node = curr_node.parent
        elif prev_node == curr_node.left:
            list_inorder.append(curr_node.data)
            if curr_node.right:
                next_node = curr_node.right
            else:
                next_node = curr_node.parent
        elif prev_node == curr_node.right:
            next_node = curr_node.parent

        prev_node = curr_node
        curr_node = next_node

    print(list_inorder)

root = Node(10)
l1 = root.add_left(7)
l2 = root.add_right(8)
l1.add_left(5)
l1.add_right(6)
inorder_iterative(root)




