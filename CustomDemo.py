class MobileNumberError(Exception):
    def __init__(self,message):
        super().__init__(message)
        print("Next Time provide 11 digit!")
    def LogError(self):
        print("Error for not providing appropriate digit in mobile number!!")