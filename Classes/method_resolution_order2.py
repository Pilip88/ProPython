class Book:
	def __init__(self, title):
		self.title = title
		self.page = 1
	def read(self):
		return 'There sure are a lot of words on page %s.' % self.page
	def bookmark(self, page):
		self.page = page


class Novel(Book):
	pass


class Mystery(Novel):
	def read(self):
		return 'Page %s and I still don\'t know who did it!' % self.page


class Product:
	def purchase(self):
		return 'Wow, you must realy like it!'


class BookProduct(Book, Product):
	pass


class MysteryProduct(Mystery, Product):
	def purchase(self):
		return 'Whodunnit?'


product1 = BookProduct('Pro Python')
print(product1.purchase())

product2 = MysteryProduct('Murder on the Orient Express')
print(product2.purchase())