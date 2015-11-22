class A:
	def test(self):
		return 'A'

class B(A):
	def test(self):
		return 'B->' + super(B, self).test()

print(B().test())

class C(A):
	def test(self):
		return 'C'

print(C().test())

class D(B, C):
	pass

print(D().test())
