class Book:
	def __init__(self, title):
		self.title = title


print(Book('Pro Python'))
print(str(Book('Pro Python')))


class BookStr:
	def __init__(self, title):
		self.title = title
	def __str__(self):
		return self.title


print(BookStr('Pro Python'))
print(str(BookStr('Pro Python')))