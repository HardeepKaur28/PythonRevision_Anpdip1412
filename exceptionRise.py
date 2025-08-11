# to check a character whether it is vowel or not
# that value should be an alphabet    raise if not alphabet
# there should be only a single character  raise when length is > 1
ch = input("Enter a character : ")

if len(ch)>1:
    try:
        raise ValueError("you should provide only one character!!")
    except ValueError as e1:
        print("Error 1 : ", e1.args)
elif  not((65 <= ord(ch) <=90) or (97 <= ord(ch) <=122)):
    try:
        raise TypeError("You should provide only alphabets for this operation")
    except TypeError as e2:
        print("Error 2 : ", e2.args)
else:
    ch1 = ch.lower()
    if ch1 in['a','e','i','o','u']:
        print(f"{ch} is a vowel")
    else:
       print(f"{ch} is a consonant")