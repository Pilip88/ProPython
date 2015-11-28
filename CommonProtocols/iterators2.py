def repeatable(generator):
	"""
	A decorator to turn a generator into an object that can be
	iterated multiple times, restarting the generator each time.
	"""
	class RepeatableGenerator:
		def __init__(self, *args, **kwargs):
			self.args = args
			self.kwargs = kwargs
		def __iter__(self):
			return iter(generator(*self.args, **self.kwargs))
	return RepeatableGenerator


@repeatable
def generator(max):
	for x in range(max):
		yield x


g = generator(5)
print(list(g))
print(list(g))