class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def __bool__(self):
		if self.width and self.height:
			return True
		return False


print(bool(Rectangle(10, 15)))
print(bool(Rectangle(0, 0)))
print(bool(Rectangle(0, 32)))