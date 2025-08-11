filename=input("Enter file name with path : ")

try:
    with open(filename, "r") as fp:
        data = fp.read()
except FileNotFoundError:
    print("File not found !! Please check the path again !! ")
except PermissionError:
    print("Permission Denied! Read operation is not permitted! !")
else:
    print("Data :\n",data)
    print("Data Read Successfully! !")