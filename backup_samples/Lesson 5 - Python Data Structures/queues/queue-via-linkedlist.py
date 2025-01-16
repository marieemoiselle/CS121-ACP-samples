class Node:
	def __init__(self, value):
		self.data = value
		self.next = None
		
# class definition of a queue
class Queue:
	def __init__(self):
		self.front = None
		self.rear = None
		
    # enqueue
	def enqueue(self, element):
		newNode = Node(element)
		if self.front is None:
			self.front = newNode
			self.rear = newNode
		else:
			self.rear.next = newNode
			self.rear = newNode
			
    # dequeue
	def dequeue(self):
		if self.front is None:
			print("Queue Underflow")
			return -1  
			# Return a sentinel value indicating error
		element = self.front.data
		self.front = self.front.next
		if self.front is None:
			self.rear = None
		return element

    # peek operation
	def peek(self):
		if self.front is None:
			print("Queue is empty")
			return -1  
			# Return a sentinel value indicating error
		return self.front.data

queue = Queue()
queue.enqueue(6)
queue.enqueue(12)
queue.enqueue(18)
queue.enqueue(24)
queue.enqueue(30)

print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Peek:", queue.peek())