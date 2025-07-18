class FirstDemo:
    a=100
    b=0
#     to define a method inside a class
    def sum(self):
        print(self.a+self.b)
    def multi(self):
        print("Product : ",self.a*self.b)
        self.sum()
# Object: we need to create an object of a class to access its variables
# and methods

ob1 = FirstDemo()
ob2 = FirstDemo()

print("ob1.a variable : ",ob1.a)
print("ob2.a variable : ",ob2.a)

print("ob1.b variable : ",ob1.b)
print("ob2.b variable : ",ob2.b)
ob1.a=200
ob2.b = 67
print("ob1.a variable : ",ob1.a)  #200
print("ob2.a variable : ",ob2.a)  #100

print("ob1.b variable : ",ob1.b)#0
print("ob2.b variable : ",ob2.b)#67

ob1.sum()
ob2.multi()