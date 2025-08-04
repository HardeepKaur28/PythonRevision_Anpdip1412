#to perform read and write operation
#open the file in a particular mode :
fp = open("D:\\coding\\python\\text.txt","r")
print(fp)
#to get data from file :
data = fp.read()
print(data)
fp.close()


#to perform write operation

fp = open("D:\\coding\\python\\abc.txt","w")
name = input("Enter your name : ")
age = input("Enter you age : ")
course = input("Enter your course : ")

print("Name : ",name)
print("Age : ",age)
print("Course : ", course)

# fp.write(name)
# fp.write(str(age))
# fp.write(course)

fp.write(name+"\t"+str(age)+"\t"+course)
print("File Saved Successfully")
fp.close()
