filename = input("Enter  filename with path : ")
fp =None
try:
    fp = open(filename, "r")
    data = fp.read()
    print("Data :\n", data)
except FileNotFoundError:
    print("No Such file found in Directory!!")
finally:
    fp.close()