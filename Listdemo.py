from itertools import count

names =["ajay","kunal","samay","sanjay","manish","lalit","umair", "Jatin"]
# len(): it is used for find the length of the list.

print("Total Elements : ", len(names))

# append(): To add more elements to the list.
# it adds elements at the end of the list.
names.append("kk")
print(names)
# names.append(["aa","bb"])

# extend() : it is used to add more than one elements to the list at the same time.
names.extend(["aa","bb"])
print(names)

# insert() : it is used to add elements at a specific index in the list.
# Also it will shift existing elements from that position to the right side.
# [11,12,13,16,18,20]
#   0,1, 2,  3, 4, 5, 6
# [11,12,23,13,16,18,20]
# now if i add 23 at 2nd index
# syntax :  listob.insert(index, value)
names.insert(2,"Aman")
print(names)

# Iteration : to access elements one by one from a given list, array etc
# in terms of loops, we can say iteration means repeating a set of instructions
# here single iteration means of running instructions for one time.
#
# for index, nm in enumerate(names):
#     print(f"Name {nm} \t index {index}")

# list(map(lambda i:print(i, names[i]),range(len(names))))
# zip() : it is used to combine together multiple statements or values
for index, nm in zip(count(), names):
    print(index, nm)

#how to find second and third occurannce in list
# lst = ['a', 'b', 'c', 'a', 'd', 'a', 'b']
#
# target = 'a'
# occurrences = [i for i, val in enumerate(lst) if val == target]
#
# if len(occurrences) >= 3:
#     print(f"2nd occurrence index: {occurrences[1]}")
#     print(f"3rd occurrence index: {occurrences[2]}")
# else:
#     print("Less than 3 occurrences found.")
