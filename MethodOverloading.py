class Demo1:
    def __init__(self):
        self.value="Parent class"

    def show(self):
        print(self.value)
class Demo2(Demo1):
    # def __init__(self):
        # self.value="Inside Child class:- demo2"
    def show(self):
        super().show()
        print("Inside child")


ob1 = Demo1()
ob2 = Demo2()

# ob1.show()
ob2.show()

# super() :it is used to call the method or variable of
# parent class. when we have method overriding or variable
# overriding, we can use super() function to access parent class
# variable or method.
