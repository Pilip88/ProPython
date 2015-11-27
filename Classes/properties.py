class Person:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
	@property
	def name(self):
	    return '%s, %s' % (self.last_name, self.first_name)
	@name.setter
	def name(self, value):
		return '%s, %s' % (self.last_name, self.first_name)
	@name.deleter
	def name(self):
		del self.first_name
		del self.last_name

p = Person('Marty', 'Alchin')
print(p.name)

p.name = 'Alchin, Martin'
print(p.name)

del p.name
print(p.name)	