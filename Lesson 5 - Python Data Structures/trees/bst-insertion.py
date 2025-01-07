class Node:
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None

def insert_node(root, value):
	if root is None:
		return Node(value)

	if value < root.data:
		root.left = insert_node(root.left, value)
	elif value > root.data:
		root.right = insert_node(root.right, value)

	return root

def inorder_traversal(root):
	if root:
		inorder_traversal(root.left)
		print(root.data, end=" ")
		inorder_traversal(root.right)

if __name__ == "__main__":
	# Create an empty BST
	root = None

	# Insert nodes into the BST
	root = insert_node(root, 42)
	root = insert_node(root, 28)
	root = insert_node(root, 63)
	root = insert_node(root, 21)
	root = insert_node(root, 35)
	root = insert_node(root, 49)
	root = insert_node(root, 70)

	# Perform inorder traversal to display the elements of the tree
	print("Inorder Traversal:")
	inorder_traversal(root)
