class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Create a singly linked list
if __name__ == '__main__':
	head = Node(5)
	second = Node(10)
	third = Node(15)

	head.next = second
	second.next = third

	# Traverse and print the elements of the linked list
	current = head
	while current:
		print(current.data, end=' ')
		current = current.next

# Output
# 5 10 15