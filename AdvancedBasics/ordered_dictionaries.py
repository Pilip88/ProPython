from collections import OrderedDict

d = OrderedDict((value, str(value)) for value in range(10) if value > 5)
print(d)

d[10] = '10'
print(d)

del d[7]
print(d)