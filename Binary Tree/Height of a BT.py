#height of a bt

class Node:
    def __init__(self, val):
        self. val = val
        self.left = None
        self. right = None
        
def height_of_bt_recursive(node):
    if node is None:
        return 0
    left_height = height_of_bt_recursive(node.left)
    right_height= height_of_bt_recursive(node.right)
    
    return 1+ max(left_height, right_height)
    
        

    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("height of a bt" , height_of_bt_recursive(root))
