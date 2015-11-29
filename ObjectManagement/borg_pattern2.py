class Base:
	def __init__(self):
		print('Base')

class Borg:
	_namespace = {}
	def __init__(self, *args, **kwargs):
		self.__dict__ = Borg._namespace
		print('Borg')

class Testing(Borg, Base):
	pass

Testing()