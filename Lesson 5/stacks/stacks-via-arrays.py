MAX_SIZE = 100

class Stack:
	def __init__(self):
		self.data = [None] * MAX_SIZE
		self.top = -1

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

stack.push(9)
stack.push(18)
stack.push(27)
stack.push(36)
stack.push(45)

print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Peek:", stack.peek())