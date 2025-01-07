from abc import ABC, abstractmethod

# Interface
class IShape(ABC):
	@abstractmethod
	def draw(self):
		pass

# Classes implementing the IShape interface
class Circle(IShape):
	def draw(self):
		print("Drawing a circle")

class Square(IShape):
	def draw(self):
		print("Drawing a square")

if __name__ == "__main__":
	circle = Circle()
	square = Square()

	circle.draw()
	square.draw()