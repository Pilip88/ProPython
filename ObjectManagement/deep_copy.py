import copy

original = [[1,2,3], [1,2,3]]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

original[0].append(4)
print(shallow_copy)
print(deep_copy)