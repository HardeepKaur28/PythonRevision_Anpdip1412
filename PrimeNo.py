class whilerange:
    def checkrange(self):
        for i in range(50,101):
            divisor=2
            is_prime=True
            while divisor<=i ** 0.5:
                if i%divisor==0:
                    is_prime = False
                    # print(f"{i} is not a prime number")
                    break
                divisor+=1
            if is_prime:
                print(f"{i} is a prime number")
obj=whilerange()
obj.checkrange()