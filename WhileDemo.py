class whiledemo:
    def countDigits(self, num):  #num=3433
        count=0
        while num!=0:  # 0!=0
            count =count+1  # count=0+1=1+1=2+1=3+1=4
            num = num//10  #  num=3433/10=343/10=34/10=3/10=0
        print("Number of Digits : ", count)

    def reverseNumber(self):
        num = int(input("enter the number"))
        # rev = ""
        rev=0
        while num > 0:
            r = num % 10
            # rev = rev + str(r)
            rev = rev*10+r
            num = num // 10
        print(rev)

    def isPrime(self,num):   # 13
        if num<=1:
           return False

        i=2
        while i*i<=num:  # 16<=13
            if num%i==0:  # 13%3==0  false
                return False
            i += 1  # i = 2+1=3+1=4
        return True
    def printPrimes(self, start, end):# start = 50 end=100
        while start<end+1:
            flag = True  # let flag= True( number is prime)
            for i in range(2, (start//2)+1):  #  i=2 i<26  50//2=25+1=26
                if start % i == 0:
                    flag = False
                    break
            if flag:
                print(start)
            start += 1


ob1 = whiledemo()
start =int(input("Enter start range : "))
end = int(input("Enter end range : "))

ob1.printPrimes(start, end)

# ob1.countDigits(int(input("Enter a number : ")))
# ob1.reverseNumber()

# num = int(input("Enter a Number : "))
# if ob1.isPrime():
#     print(num," is prime number")
# else:
#     print(num," is not a prime number")

# Q1. wap to reverse a number
# eg. num=193931   rev= 139391
# Q2.  wap to check whether a number is prime or not.
# Q3. wap to print all prime number between a given range.
#  input start range :=50
# input end range : 100
# print primes between 50 to 100