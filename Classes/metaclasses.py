class SimpleMetaclass(type):
	def __init__(cls, name, bases, attrs):
		print(name)
		super(SimpleMetaclass, cls).__init__(name, bases, attrs)


class Example(metaclass=SimpleMetaclass):
	pass

