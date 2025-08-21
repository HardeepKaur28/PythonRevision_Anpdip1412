
# Tuple :
# -------
# - Tuple is an inbuilt data structure.
# - It is used to store multiple items in a single variable and we can have elements of heterogeneous type.
# - Tuple is immutable in nature i.e. we can't add or remove or modified elements once a tuple is created.
# - Tuple can store duplicate values.
# - tuple is usually defined using the brackets().
#
# => to create an Empty tuple:-
# 	ob = ()
# => to create a tuple with multiple values:-
# 	ob = (value1, value2, value3, ....valuen)
# => Single valued tuple
# 	ob =(value,)
#
# => tuple using constructure
# 	ob = tuple((value1, value2, value3....))
#
# =>type(): to determine the type of a tuple
# => len() : to determine the length of a tuple.
# => max() and min() : it returns the maximum and minimum value from the tuple.
# => sum() : it returns the sum of all the elements.
#
# => to convert a list into a tuple
# 	ob = tuple(listob)
# => count() : it is used to count the occurrences of an element.
# 	ob.count(value)
# => index() : it is used to find the index of an element. If the tuple contains multiple copies of the same value, then it returns the index of the first occurrence.
# 	ob.index(value)
# => concatenation : to join multiple sets of tuples we use + operator
# 	ob = t1+t2+t3...
# => repetition : to repeat a set of tuples for the given number of times we use * operator
# 	t1*number
# => in and not in (membership operators) :
# we can use in and non in operators in tuples to find the values also.
# => Iteration in tuple: to access each element one by one.
# for var in tuplename:
# 	print(var)
# 	use var for any maninpulations



# empty tuple
ob1 = ()

ob2 = (12,99.23,"dkme","kdke",3435,35,24.556, "heke")

ob3 = ("anudip",)

ob4 =tuple(("abc","def",13,55,'ddd'))

print("ob1 : ",ob1)
print("ob1 type : ", type(ob1))
print("ob2 : ",ob2)
print("ob2 type : ", type(ob2))
print("ob3 : ",ob3)
print("ob3 type : ", type(ob3))
print("ob4 : ", ob4)
print("Ob4 length : ", len(ob4))
ob5 =(24,35,12,89,49,24,96,34)

print("max from ob5 : ", max(ob5))
print("min from ob5 : ", min(ob5))
print("Sum of all elements : ", sum(ob5))

list1 = [1,2,3,4,5,6,7,8,9,10]
ob6 = tuple(list1)
print("ob6 : ", ob6)
print("Occurrences of  24 in ob5 : ", ob5.count(24))
print("Index of 35 :  ", ob5.index(35))
print('concatenation : ', ob2+ob3)
print("ob3 repeat for 2 times : ", ob3*2)
print("find 8 in ob6 : ", 8 in ob6)

for x in ob6:
    print(x)