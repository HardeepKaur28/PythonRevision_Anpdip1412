print("Enter two number: ")
a=int(input())
b=int(input())
try:
    result = a/b
    print("Division : ",result)
except ZeroDivisionError:
    print("You have provided 0 to divide with",a)
    print("Try Again later")