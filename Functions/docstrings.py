import inspect

def divide(x, y):
	"""
	divide(integer, integer) -> floating point
	This is a more complex example, with more comperhensive documentation.
	"""
	return x/y

print(divide.__doc__)

print(inspect.getdoc(divide))