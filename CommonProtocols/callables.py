class CallCounter:
	def __init__(self):
		self.count = 0
	def __call__(self, *args, **kwargs):
		self.count += 1
		return 'Number of calls so far: %s' % self.count
	def reset(self):
		self.count = 0

counter = CallCounter()
print(counter())
print(counter())
counter.reset()
print(counter())
