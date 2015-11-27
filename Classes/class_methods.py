class Example:
	@classmethod
	def method(cls):
		return cls


class ExampleMeta(type):
	def method_meta(cls):
		return cls


class Example2(metaclass=ExampleMeta):
	pass


print(Example.method)
print(Example.method())
print(Example().method())


print(Example2.method_meta)
print(Example2.method_meta())