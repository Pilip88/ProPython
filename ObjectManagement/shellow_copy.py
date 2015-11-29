import copy

class Example:
	def __init__(self, value):
		self.value = value


a = Example('spam')
b = copy.copy(a)
b.value = 'eggs'

print(a.value)
print(b.value)