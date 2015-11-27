class Example:
	def method(self):
		return 'done!'

# Unbound method
print(type(Example.method))
print(Example.method)
#Example.method() raises an error

# Bound method
e = Example()
print(type(e.method))
print(e.method)
print(e.method())
