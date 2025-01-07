MAX_SIZE = 5

class Stack:
	def __init__(self):
		self.data = [None] * MAX_SIZE 
		#list to store the elements
		self.top = -1
		#keeps track of the position of the last element added

    # push operation
	def push(self, element):
		if self.top == MAX_SIZE - 1:
			print("Stack Overflow")
			return
		self.top += 1
		self.data[self.top] = element

    # pop operation
	def pop(self):
		if self.top == -1:
			print("Stack Underflow")
			return -1  
		    # sentinel value indicating error
		element = self.data[self.top]
		self.top -= 1
		return element

    # peek operation
	def peek(self):
		if self.top == -1:
			print("Stack is empty")
			return -1  
		    # sentinel value indicating error
		return self.data[self.top]

stack = Stack()


print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Peek:", stack.peek())