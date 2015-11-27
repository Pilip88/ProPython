class Calc:
	def __init__(self, value):
		self.value = value
	def __add__(self, add_value):
		self.value += add_value
		return self.value
	def __radd__(self, add_value):
		self.value += add_value
		return self.value
	def __sub__(self, sub_value):
		self.value -= sub_value
		return self.value
	def __rsub__(self, sub_value):
		self.value = sub_value - self.value
		return self.value
	def __mul__(self, mul_value):
		self.value *= mul_value
		return self.value
	def __rmul__(self, mul_value):
		self.value *= mul_value
		return self.value
	def __truediv__(self, true_div_value):
		self.value /= true_div_value
		return self.value
	def __rtruediv__(self, true_div_value):
		self.value = true_div_value / self.value
		return self.value
	def __floordiv__(self, floor_div_value):
		self.value //= floor_div_value
		return self.value
	def __rfloordiv__(self, floor_div_value):
		self.value = true_div_value // self.value
		return self.value
	def __mod__(self, mod_value):
		self.value %= mod_value
		return self.value
	def __rmod__(self, mod_value):
		self.value = mod_value % self.value
		return self.value
	def __pow__(self, pow_value):
		self.value **= pow_value
		return self.value