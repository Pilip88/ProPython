def fact(n):
	"""Returns factorial of given number"""
	solution = 1
	while n > 0:
		solution *= n
		n -= 1

	return solution


print(fact(2))
print('-'*10)
print(fact(4))
print('-'*10)
print(fact(10))
print('-'*10)

