import heapq

class PriorityQueue:
	def __init__(self):
		self.elements = []
	
	def enqueue(self, data, priority):
		new_element = (priority, data)
		heapq.heappush(self.elements, new_element)
	
	def dequeue(self):
		if not self.elements:
			print("Priority queue is empty. Dequeue operation failed.")
			return None
		
		return heapq.heappop(self.elements)[1]


queue = PriorityQueue()

queue.enqueue("peach", 2)
queue.enqueue("cherry", 1)
queue.enqueue("strawberry", 3)

print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())