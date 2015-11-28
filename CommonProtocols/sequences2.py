class Range:

	def __init__(self, a, b=None, step=1):
		"""
		Define a range according to a starting value, an end value and a step.
		If only one argument is provided, it's taken to be the end value. If
		two arguments are passed in, the first becomes a start value, while the
		second is the end value. An optional step can be provided to control
		how far apart each value is from the next.
		"""
		if b is not None:
			self.start = a
			self.end = b
		else:
			self.start = 0
			self.end = a
		self.step = step

	def __getitem__(self, key):
		if isinstance(key, slice):
			r = range(key.start or 0, key.stop, key.step or 1)
			return [self.step * val + self.start for val in r]
		value = self.step * key + self.start
		if value < self.end:
			return value
		else:
			raise IndexError('key outside of the given range')


r = Range(5)
print(list(r))
print(r[3])

r = Range(3, 17, 4)
print(list(r))
print(r[2])
