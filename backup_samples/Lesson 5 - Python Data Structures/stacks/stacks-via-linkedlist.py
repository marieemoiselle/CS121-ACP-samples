class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.top = None

    # push operation
	def push(self, element):
		new_node = Node(element)
		new_node.next = self.top
		self.top = new_node

    # pop operation
	def pop(self):
		if self.top is None:
			print("Stack Underflow")
			return -1  
			# Sentinel value indicating error
		element = self.top.data
		self.top = self.top.next
		return element

    # peek operation
	def peek(self):
		if self.top is None:
			print("Stack is empty")
			return -1  
			# Sentinel value indicating error
		return self.top.data

stack = Stack()

stack.push(7)
stack.push(14)
stack.push(21)
stack.push(28)
stack.push(35)

print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Peek:", stack.peek())