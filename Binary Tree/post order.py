#postorder traversal in BT
#  Left Right  Root

class Node:
    def __init__(self, val):
        self. val = val
        self.left = None
        self. right = None
        
def postorder_traversal(node, arr):
    if node is None:
        return
    postorder_traversal(node.left, arr)
    postorder_traversal(node.right,arr)
    arr.append(node.val)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


result = []
postorder_traversal(root, result)
print("Postorder Traversal:", result)
