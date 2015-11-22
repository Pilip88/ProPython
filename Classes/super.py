class A:
	def afunction(self):
		print('afunction from class A')

class B(A):
	def __init__(self):
		print('B is constructed!!!')
	def afunction(self):
		return super(B, self).afunction()


sample1 = B()
sample1.afunction()