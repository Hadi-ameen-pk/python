import copy
nested_list = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(nested_list)
shallow_copy[0][0] = 99
print(nested_list)
print(shallow_copy)
