a=100

b = 23.48
c=2j+8
print(f"a : {a} \tb : {b} \tc : {c}")
print("Data types of variables : ")
print(f"a : {type(a)} \tb : {type(b)} \tc : {type(c)}")

print("-"*56)
str = "Welcome To Python"
print("str : " , str)
print("str[3] : " , str[3])
print("str[-2] : ", str[-2])
print("from index 2 to 8 : ", str[2:8])
print("Reverse string : " , str[::-1])
print("Sub String using negative index : " , str[-5:-1])
print("Reverse sub string : " , str[-1:-5:-1])

print("-"*56)
emp = ['e101' , 'jai' , 34 , 78000.38]
print('emp : ',emp)
print("type : " , type(emp))
print("Name : " , emp[1])
print("Agw : " ,emp[2])
print(emp[1:3])
print(emp[::2])
print(emp[::3])
emp.insert(4,"Delhi")
print(emp)
emp.append("read,write")
print(emp)

list2 = ['aa','bb','cc']
emp.append(list2)
print(emp)
