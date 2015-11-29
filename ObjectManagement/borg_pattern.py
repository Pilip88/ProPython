class Borg:
	_namespace = {}
	def __init__(self):
		self.__dict__ = Borg._namespace


a = Borg()
b = Borg()
print(hasattr(a, 'attribute'))
b.attribute = 'value'
print(hasattr(a, 'attribute'))
print(a.attribute)
print(Borg._namespace)