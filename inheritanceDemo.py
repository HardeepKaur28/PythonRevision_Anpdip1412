class Calc :
    def add (self,a,b):
        print("Sum : ",a+b)
    def sub(self,a,b):
        print("Difference : ",a-b)

class Calculator:
    def add(self,a,b):
        s1=0
        for i in a:
            s1 = s1+i
        print("Sum of List 1 : ",s1)
        s2= sum(b)
        print("Sum of List 2 : ",s2)
        print("Sum of list1 and list2 : " , s1+s2)

class UserDemo(Calculator,Calc):

    def Demo1(self):
        list1 = [12,44,66,33,89,22]
        list2 = [35,94,29,998,29,32]
        self.add(list1,list2)
        # self.add(345,933)


ob1 = UserDemo()
ob1.Demo1()
#ob1.add(34,66)