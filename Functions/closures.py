def multiply_by(factor):
	"""Return a function that multiplies values by the given factor"""
	def multiply(value):
		"""Multiply the given value by the factor already provided"""
		return value * factor
	return multiply

times2 = multiply_by(2)
print(times2(2))