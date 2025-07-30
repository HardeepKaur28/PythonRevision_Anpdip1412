class Demo2 :
    a = 0
    b=0
    def __init__(self,x,y=None,z=None):
        print("x : " ,x)
        print("y : ",y)
        print("z : " , z)


obj1 = Demo2(10)
obj2 = Demo2(100,200)
obj3 = Demo2(1000,2000,3000)
