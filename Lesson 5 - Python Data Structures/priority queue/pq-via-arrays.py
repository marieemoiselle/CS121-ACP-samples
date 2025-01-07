class PriorityQueue:
	def __init__(self):
		self.elements = []
	
	def enqueue(self, data, priority):
		new_element = (data, priority)
		self.elements.append(new_element)
		self.elements.sort(key=lambda x: x[1])
	
	def dequeue(self):
		if not self.elements:
			print("Priority queue is empty. Dequeue operation failed.")
			return None
		
		return self.elements.pop(0)[0]


queue = PriorityQueue()

#the lower the numerical value, the higher the priority
queue.enqueue("hello", 2)
queue.enqueue("python", 1)
queue.enqueue("world", 3)

print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())