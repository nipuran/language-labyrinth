class Rectangle():
	length: int = None
	width: int = None

	def __init__(self, length, width):
		self.length = length
		self.width = width

	def size(self):
		return self.length * self.width

rec1 = Rectangle(34, 55)
size = Rectangle.size(rec1)
print(size)
