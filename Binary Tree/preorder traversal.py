#preorder traversal in BT
# Root Left Right 

class Node:
    def __init__(self, val):
        self. val = val
        self.left = None
        self. right = None
        
def preorder_traversal(node, arr):
    if node is None:
        return
    arr.append(node.val)
    preorder_traversal(node.left, arr)
    
    preorder_traversal(node.right,arr)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


result = []
preorder_traversal(root, result)
print("Preorder Traversal:", result)
