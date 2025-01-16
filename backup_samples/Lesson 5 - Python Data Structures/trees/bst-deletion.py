class Node:
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None

def find_min_value(node):
	current = node
	while current.left is not None:
		current = current.left
	return current

def delete_node(root, value):
	if root is None:
		return root

	if value < root.data:
		root.left = delete_node(root.left, value)
	elif value > root.data:
		root.right = delete_node(root.right, value)
	else:
		if root.left is None:
			temp = root.right
			return temp
		elif root.right is None:
			temp = root.left
			return temp

		successor = find_min_value(root.right)
		root.data = successor.data
		root.right = delete_node(root.right, successor.data)

	return root

def inorder_traversal(root):
	if root:
		inorder_traversal(root.left)
		print(root.data, end=" ")
		inorder_traversal(root.right)

if __name__ == "__main__":
	# Create a binary search tree: 
	# 24 -> 16 -> 36 -> 12 -> 20 -> 32 -> 40
	root = Node(24)
	root.left = Node(16)
	root.right = Node(36)
	root.left.left = Node(12)
	root.left.right = Node(20)
	root.right.left = Node(32)
	root.right.right = Node(40)

	# Delete nodes from the binary search tree
	root = delete_node(root, 12)
	root = delete_node(root, 16)
	root = delete_node(root, 36)

	# Perform inorder traversal to display the elements of the remaining tree
	print("Inorder Traversal after Deletion:")
	inorder_traversal(root)
