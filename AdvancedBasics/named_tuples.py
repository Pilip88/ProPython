from collections import namedtuple

Point = namedtuple('Point', 'x y z')
point = Point(12,34,56)
print(point)

print(point.x)
print(point.y)
print(point.z)

print(point[0])
print(point[1])
print(point[2])