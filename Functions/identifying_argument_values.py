import inspect

def example(a=1, b=1, *c, d, e=2, **f) -> str:
	pass

def get_arguments(func, args, kwargs):
	"""
	Given a function and a set of arguments,
	return a dictionary of argument values
	that will be sent to the function.
	"""
	arguments = kwargs.copy()
	spec = inspect.getfullargspec(func)
	arguments.update(zip(spec.args, args))
	return arguments

print(get_arguments(example, (1,), {'f':4}))
