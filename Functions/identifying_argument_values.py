import inspect

def example(a=1, b=1, *c, d, e=2, **f):
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

	if spec.defaults:
		for i, name in enumerate(spec.args[-len(spec.defaults):]):
			if name not in arguments:
				arguments[name] = spec.defaults[i]

	return arguments

print(get_arguments(example, (1,), {'f':4}))
