class Money:
	def __init__(self, amount, currency):
		self.amount = amount
		self.currency = currency
		self.conversion = {'USD': 1, 'CAD': .95}
	def __str__(self):
		return '%.2f %s' % (self.amount, self.currency)
	def __repr__(self):
		return 'Money(%r, %r)' % (self.amount, self.currency)
	def in_currency(self, currency):
		ratio = self.conversion[currency] / self.conversion[self.currency]
		return Money(self.amount * ratio, currency)