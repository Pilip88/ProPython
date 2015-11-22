print(isinstance(10, int))

print(isinstance('test', tuple))

print(issubclass(int, object))

class A:
	pass

class B(A):
	pass

print(issubclass(B, A))

print(issubclass(B, B))

print(B.__bases__)

print(A.__subclasses__())

print(B.__mro__)
