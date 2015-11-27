class Book:
	def __init__(self, title, author=None):
		self.title = title
		self.author = author
	def __str__(self):
		return self.title
	def __repr__(self):
		return '<%s by %s>' % (self.title, self.author or '<Unknown Author>')


print(Book('Pro Python', author='Marty Alchin'))
Book('Some Book')