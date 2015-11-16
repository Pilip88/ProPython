import inspect

def example(a=1, b=1, *c, d, e=2, **f) -> str:
	pass

print(inspect.getfullargspec(example))
