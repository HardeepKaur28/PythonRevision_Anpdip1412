class Patterns:
    def pattern1(self, rows):  # rows=5
        for row in range(1, rows+1): # row=1 2 3 row<6
            for col in range(1, row+1):  # col = 1 2 3  col < 3+1=4
                print(col, end=" ") # print 2
            print()  # to bring the cursor to next line


ob1 = Patterns()
ob1. pattern1(5)
# 1
# 1 2
#