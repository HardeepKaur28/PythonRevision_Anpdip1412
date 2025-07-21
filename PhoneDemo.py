import time

class BasicPhone:
    def makeCall(self,phoneNumber):
        print("Making call....")
        time.sleep(2)
        print("Call Connect With " , phoneNumber)

    def sms(self,phoneNumber):
        msg = input("Enter your message : ")
        print("Sending message to ", phoneNumber)
        print("Message sent Successfully!!")
        print("Sent Message is : \n",msg)


class SmartPhone(BasicPhone):
    def openPlayStore(self):
        app = input("Enter app name : ")
        print("Starting downloading for ",app)
        print(app, "installed successfully!!")


obj1 = SmartPhone()
print("Enter phone number : ")
obj1.makeCall(input())
obj1.openPlayStore()