example = {1, 2, 3, 4, 5}
print('example = ' + str(example))
print('1 in example = ' + str(1 in example))
print('6 in example = ' + str(6 in example))

example.add(6)
print(example)
example.add(6)
print(example)

example.update({7, 8, 9, 10})
print(example)

example.remove(10)
print(example)

example.discard(9)
print(example)

print(example.pop())

example.clear()
print(example)