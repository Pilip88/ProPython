first_set = {1,2,3}
second_set = {1,2,3,4,5,6}

print(first_set.issubset(second_set)) # True
print(second_set.issubset(first_set)) # False

print(first_set.issuperset(second_set)) # False
print(second_set.issuperset(first_set)) # True

print(first_set.issubset(first_set)) # True
print(first_set.issuperset(first_set)) # True