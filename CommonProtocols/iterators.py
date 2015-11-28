class Range:
	def __init__(self, count):
		self.count = count
	def __iter__(self):
		return RangeIter(self.count)

class RangeIter:
	def __init__(self, count):
		self.count = count
		self.current = 0
	def __iter__(self):
		return self
	def __next__(self):
		value = self.current
		self.current += 1
		if self.current > self.count:
			raise StopIteration
		return value


def range_gen(count):
	for x in range(count):
		yield x


r = range_gen(5)
print(list(r))
print(list(r))

r = Range(5)
print(list(r))
print(list(r))

r = RangeIter(10)
print(list(r))