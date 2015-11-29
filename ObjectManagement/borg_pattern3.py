class Base:
	def __init__(self):
		print('Base')


class Borg:
	_namespace = {}
	def __new__(cls, *args, **kwargs):
		print('Borg')
		obj = super(Borg, cls).__new__(cls, *args, **kwargs)
		obj.__dict__ = cls._namespace
		return obj


class Testing(Borg, Base):
	pass


Testing()