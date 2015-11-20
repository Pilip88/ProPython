def fibonacci(count):
	a, b = -1, 1

	while count > 0:
		c = a + b
		yield c

		a, b = b, c
		count -= 1

for x in fibonacci(3):
	print(x)

for c in fibonacci(20):
	print(c)