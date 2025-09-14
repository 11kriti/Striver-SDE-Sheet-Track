def inorder_traversal(node, arr):
    if node is None:
        return
    inorder_traversal(node.left, arr)
    arr.append(node.val)
    inorder_traversal(node.right,arr)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

result = []
inorder_traversal(root, result)
print("Inorder Traversal:", result)
