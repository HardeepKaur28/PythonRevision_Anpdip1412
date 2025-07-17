# password length >=8
# atleast one character should be capital, small, numeric value, special
# character
#There should be no space in password
import re
passwd = input("Enter password : ")
c1 = len(passwd) >= 8
c2 = (((bool(re.search(r'[A-Z]',passwd)) and
      bool(re.search(r'[a-z]',passwd))) and
      bool(re.search(r'[0-9]',passwd))) and
      bool(re.search(r'[@#$%^&*_-]',passwd)))

c3 = bool(re.search(r'[^A-Za-z0-9_#]',passwd))
print(c1)
print(c2)
print(c3)
if c1 and c2:
    print("Password strength is good")
else:
    print("Password should contain at least one character of each[^A-Za-z0-9_#]")






