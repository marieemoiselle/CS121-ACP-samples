class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def preorder_traversal(node):
	if node is None:
		return

	print(node.data, end=' ') 
	# Process current node

	preorder_traversal(node.left) 
	# Traverse left subtree

	preorder_traversal(node.right) 
	# Traverse right subtree

# Construct a sample binary tree
root = Node(9)
root.left = Node(18)
root.right = Node(27)
root.left.left = Node(36)
root.left.right = Node(45)

# Perform preorder traversal on the binary tree
print("Preorder Traversal: ", end='')
preorder_traversal(root)
print()