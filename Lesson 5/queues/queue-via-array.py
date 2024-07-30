class Queue:
	def __init__(self):
		self.data = []
		self.front = 0
		self.rear = -1

    # enqueue
	def enqueue(self, element):
		self.data.append(element)
		self.rear += 1

    # dequeue
	def dequeue(self):
		if self.front > self.rear:
			print("Queue Underflow")
			return -1  
		    # sentinel value indicating error
		element = self.data[self.front]
		self.front += 1
		return element

	def peek(self):
		if self.front > self.rear:
			print("Queue is empty")
			return -1  
		    # sentinel value indicating error
		return self.data[self.front]

queue = Queue()
queue.enqueue(4)
queue.enqueue(8)
queue.enqueue(12)
queue.enqueue(16)
queue.enqueue(20)

print("Peek:", queue.peek())
print("Dequeue:", queue.dequeue())
print("Peek:", queue.peek())