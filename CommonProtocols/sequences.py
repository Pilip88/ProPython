class Range:
	def __init__(self, max):
		self.max = max
	def __iter__(self):
		for x in range(self.max):
			yield x
	def __len__(self):
		return self.max
	def __reversed__(self):
		for x in range(self.max - 1, -1, -1):
			yield x