class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def postorder_traversal(node):
	if node is None:
		return

	postorder_traversal(node.left)  
	# Traverse left subtree

	postorder_traversal(node.right)  
	# Traverse right subtree

	print(node.data, end=' ')  
	# Process current node

# Construct a sample binary tree
root = Node(9)
root.left = Node(18)
root.right = Node(27)
root.left.left = Node(36)
root.left.right = Node(45)

# Perform postorder traversal on the binary tree
print("Postorder Traversal: ", end='')
postorder_traversal(root)
print()
