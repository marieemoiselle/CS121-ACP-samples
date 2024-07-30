class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Recursive search in a BST
def search_recursive(root, target):
	if root is None or root.data == target:
		return root

	if target < root.data:
		return search_recursive(root.left, target)

	return search_recursive(root.right, target)

# Iterative search in a BST
def search_iterative(root, target):
	while root is not None and root.data != target:
		if target < root.data:
			root = root.left
		else:
			root = root.right

	return root

def insert(root, key):
	if root is None:
		return Node(key)

	if key < root.data:
		root.left = insert(root.left, key)
	else:
		root.right = insert(root.right, key)

	return root

def inorder_traversal(root):
	if root:
		inorder_traversal(root.left)
		print(root.data, end=" ")
		inorder_traversal(root.right)

if __name__ == "__main__":
	root = Node(48)
	insert(root, 32)
	insert(root, 72)
	insert(root, 24)
	insert(root, 40)
	insert(root, 64)
	insert(root, 80)

	print("Inorder Traversal:")
	inorder_traversal(root)
	print()

	target = 32
	result_recursive = search_recursive(root, target)
	if result_recursive:
		print(f"Recursive: Found {target}")
	else:
		print(f"Recursive: Not Found")

	result_iterative = search_iterative(root, target)
	if result_iterative:
		print(f"Iterative: Found {target}")
	else:
		print(f"Iterative: Not Found")
