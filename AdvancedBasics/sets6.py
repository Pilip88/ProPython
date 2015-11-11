first_set = {1,2,3,4,5,6,7}
second_set = {6,7,8,9,10}

symmetric_difference_set = first_set ^ second_set
print(symmetric_difference_set)

second_symmetric_difference_set = first_set.symmetric_difference(second_set)
print(second_symmetric_difference_set)