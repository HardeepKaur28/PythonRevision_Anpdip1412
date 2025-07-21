class Demo1:
    a=0

    def __init__(self):
        print("Defaut Constructor")
    def __init__(self ,a = None):
        print("New object is being created")
        self.a = 10
        print(a)
        print(self.a)


obj1 = Demo1(100)
obj2 = Demo1(200)
obj3 = Demo1()
