class Node:
	def __init__(self, data):
		self.data = data
		self.previous = None
		self.next = None

# Create a doubly linked list
if __name__ == '__main__':
	head = Node("Fatima Marie")
	second = Node("Kenneth Joshua")
	third = Node("Arjonel")

	head.next = second
	second.previous = head
	second.next = third
	third.previous = second

	# Traverse and print the elements of the linked list
	print("Linked List:")
	current = head
	while current:
		if current.next is None:
			print(current.data)
		else:
			print(current.data, end=' <-> ')
		current = current.next