my_set = {1,2,2,3,4,4,4}
print("Set :" , my_set)
my_set.add(5)
print("Updated set :", my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)
result = set1.intersection(set2)
print(result)
result = set1.difference(set2)
print(result)
result = set1.symmetric_difference(set2)
print(result)

