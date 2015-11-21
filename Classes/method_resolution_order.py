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


book1 = Book('Pro Python')
print(book1.read())

book1.bookmark(page=52)
print(book1.read())

book2 = Novel('Pride and Prejustice')
print(book2.read())

book3 = Mystery('Murder on the Orient Express')
print(book3.read())

book3.bookmark(page=352)
print(book3.read())