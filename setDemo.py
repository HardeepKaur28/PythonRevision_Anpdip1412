set1 = {"aa","bb","dd",24,35,13,45.24, "aa",35}
set2 = set((33,35,"aa","bb","kk","dg"))
print(set1)
print(set2)

set1.add(90)
set1.add(35)
print("set1 : ", set1)

set1.update([100,200,300])
print("set1 : ", set1)

set1.remove(13)
print("set1 after removing 13 : ", set1)

set1.discard(48)
print("set1  : ", set1)

print("pop : ", set1.pop())

print("set1 : ",set1)
print("set2 : ",set2)

print("Union : ", set1.union(set2))
print("Union : ", set1 | set2)

print('intersection : ', set1.intersection(set2))
print('intersection : ', set1 & set2)

print("Difference : ", set1.difference(set2))
print("Difference : ", set1 - set2)

print("symmetric difference : ", set1.symmetric_difference(set2))
print("symmetric difference : ", set1 ^ set2)