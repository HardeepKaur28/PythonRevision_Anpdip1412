
# raise mobile number exception

from CustomDemo import MobileNumberError
mobile = input("Enter mobile number : ")
if len(mobile)>11 or len(mobile)<11:
    try:
        raise MobileNumberError("Mobile Number Error !! ")
    except MobileNumberError as mm:
        print("Error : ", mm.args)
        mm.LogError()
else:
    print ("Mobile number is valid!!")