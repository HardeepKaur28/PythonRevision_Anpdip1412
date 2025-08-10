# r = 6
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end = " ")
#     print()

# for m in range(1,6):
#     for n in  range(1,m+1):
#         print("+",end = " ")
#     print()

# r = 5
# for i in range(r):
#     for j in range(i,r):
#         print("+",end =" ")
#     print()

n=5
# for i in range(n):
#
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("+",end =' ')
#     print()

# for i in range(n):
#
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("+",end =' ')
#     print()

# for i in range(n):
#
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("+",end =' ')
#     for i in range(i+1):
#         print("+",end=' ')
#     print()

# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*", end=" ")
#     print()

# n = 5
#
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#          print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#          print("*",end=" ")
#     print()

# n=5
# p=1
# for i in range(n):
#     for j in range(i+1):
#         print(p, end =" ")
#     p+=1
#     print()

# n=5
# p=1
# for i in range(n):
#     for j in range(i,n):
#         print(p, end =" ")
#     p+=1
#     print()

# n=5
# p=5
# for i in range(n):
#     for j in range(i+1):
#         print(p, end =" ")
#     p-=1
#     print()

# n=5
# p=5
# for i in range(n):
#     for j in range(i,n):
#         print(p, end =" ")
#     p-=1
#     print()

# n=5
# p=0
# for i in range(n):
#     for j in range(i+1):
#         print(p, end =" ")
#     p+=2
#     print()

# n=5
#
# for i in range(n):
#     for j in range(i+1):
#        if(i%2==0):
#            print("1",end=" ")
#        else:
#            print("2",end=" ")
#
#     print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#        if(i%2==0):
#            print("$",end=" ")
#        else:
#            print("#",end=" ")
#     print()

# n=5
# p=1
# for i in range(n-1):
#     for j in range(i,n):
#      print(" ",end=" ")
#     for j in range(i):
#         print(p,end=" ")
#     for j in range(i+1):
#         print(p,end=" ")
#     p+=1
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print(p,end=" ")
#     for j in range(i,n):
#         print(p,end=" ")
#     p+=1
#     print()

# n=5
# p=1
# for i in range(n-1):
#     for j in range(i,n):
#      print(" ",end=" ")
#     for j in range(i):
#         print(p,end=" ")
#     for j in range(i+1):
#         print(p,end=" ")
#     p+=1
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print(p,end=" ")
#     for j in range(i,n):
#         print(p,end=" ")
#     p-=1
#     print()

# n=5
# for i in range(n):
#     p=1
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     print()

# n=5
# for i in range(n):
#     p=1
#     for j in range(i,n):
#         print(p,end=" ")
#         p+=1
#     print()

# n=5
# for i in range(n):
#     p=5
#     for j in range(i+1):
#         print(p,end=" ")
#         p-=1
#     print()

# n=5
# k=5
# for i in range(n):
#     p=k
#     for j in range(i,n):
#         print(p,end=" ")
#         p-=1
#     k-=1
#     print()

# n=5
# k=5
# for i in range(n):
#     p=k
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(p,end=" ")
#         p-=1
#     k-=1
#     print()

# n=4
# p=1
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#         p+=1
#     print()


#           1
#         1 2 1
#       1 2 3 2 1
#     1 2 3 4 3 2 1
#   1 2 3 4 5 4 3 2 1

# n=5
# for i in range(n):
#     p=1
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print(p,end=" ")
#         p+=1
#     for j in range(i+1):
#         print(p,end=" ")
#         p-=1
#     print()

# character  pattern :

# A
# B B
# C C C
# D D D D
# E E E E E

# n=5
# c=65
# for i in range(n):
#     for j in range(i+1):
#         print(chr(c),end=" ")
#     c+=1
#     print()

# A
# A B
# A B C
# A B C D
# A B C D E

# n=5
# for i in range(n):
#     c = 65
#     for j in range(i+1):
#         print(chr(c),end=" ")
#         c+=1
#     print()

# A
# B B
# A A A
# B B B B
# A A A A A
# n=5
# c=65
# for i in range(n):
#     for j in range(i+1):
#         if(i%2==0):
#             print("A",end=" ")
#         else:
#             print("B",end=" ")
#         c+=1
#     print()

# n=5
# c=65
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=' ')
#     for j in range(i):
#         print(chr(c),end=" ")
#     for j in range(i+1):
#         print(chr(c),end=" ")
#     c+=1
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print(chr(c),end=" ")
#     for j in range(i,n):
#         print(chr(c),end=" ")
#     c+=1
#     print()

# change pattern in column
# A
# A B
# A B C
# A B C D
# A B C D E

# n=5
# for i in range(n):
#     c = 65
#     for j in range(i+1):
#         print(chr(c),end=" ")
#         c+=1
#     print()

#   A B C D E
#     A B C D
#       A B C
#         A B
#           A
# n=5
# for i in range(n):
#     c = 65
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(chr(c),end=" ")
#         c+=1
#     print()

#           A
#         A B C
#       A B C D E
#     A B C D E F G
#   A B C D E F G H I

# n=5
# for i in range(n):
#     c=65
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print(chr(c),end=" ")
#         c+=1
#     for j in range(i+1):
#         print(chr(c),end=" ")
#         c+=1
#     print()

# E
# E D
# E D C
# E D C B
# E D C B A
# n=5
# for i in range(n):
#     c=69
#     for j in range(i+1):
#         print(chr(c),end=" ")
#         c-=1
#     print()

#   E D C B A
#     E D C B
#       E D C
#         E D
#           E
# n=5
# k=69
# for i in range(n):
#     c=k
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(chr(c),end=" ")
#         c-=1
#      k-=1
#     print()

#           A
#         A B A
#       A B C B A
#     A B C D C B A
#   A B C D E D C B A
# n=5
# for i in range(n):
#     c=65
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print(chr(c),end=" ")
#         c+=1
#     for j in range(i+1):
#         print(chr(c),end=" ")
#         c-=1
#     print()

# C
# O O
# D D D
# E E E E
# R R R R R
# s="CODER"
# n=len(s)
# p=0
# for i in range(n):
#     for j in range(i+1):
#         print(s[p],end=" ")
#     p+=1
#     print()

# string reverse program
# R
# E E
# D D D
# O O O O
# C C C C C

# s="CODER"
# n=len(s)
# p=n-1
# for i in range(n):
#     for j in range(i+1):
#         print(s[p],end=" ")
#     p-=1
#     print()

# change patter in column
# C
# C O
# C O D
# C O D E
# C O D E R
# s="CODER"
# n=len(s)
# for i in range(n):
#     p=0
#     for j in range(i+1):
#         print(s[p],end=" ")
#         p+=1
#     print()

# starting character same :
# R
# R E
# R E D
# R E D O
# R E D O C

# s="CODER"
# n=len(s)
# for i in range(n):
#     p = n - 1
#     for j in range(i+1):
#         print(s[p],end=" ")
#         p-=1
#     print()

# starting character is different :
#   R R R R R
#     E E E E
#       D D D
#         O O
#           C
# s="CODER"
# n=len(s)
# p = n - 1
# for i in range(n):
#     k=p
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(s[p],end=" ")
#         k-=1
#     p-=1
#     print()

# Hollow Patterns:

# *       *
# *       *
# *       *
# *       *
# *       *

# n=5
# for i in range(n):
#     for j in range(n):
#         if(j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=' ')
#     print()

#     *
#     *
# * * * * *
#     *
#     *

# n=5
# for i in range(n):
#     for j in range(n):
#         if(i==n//2 or j==n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=' ')
#     print()

# *       *
#   *   *
#     *
#   *   *
# *       *

# n=5
# for i in range(n):
#     for j in range(n):
#         if(i==j or i+j == n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=' ')
#     print()

# * * * * *
# *       *
# *       *
# *       *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(n):
#         if(i==0 or  j==0 or i==n-1 or j== n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=' ')
#     print()

# Hollow triangle :

# *
# * *
# *   *
# *     *
# * * * * *

# n=5
# for i in range(n):
#     for j in range(i+1):
#         if(j==0 or i==n-1 or i==j ):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# * * * * *
# *     *
# *   *
# * *
# *

# n=5
# for i in range(n):
#     for j in range(i,n):
#         if( i==0 or j==i or j==n-1 ):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

#           *
#         *   *
#       *       *
#     *           *
#   * * * * * * * * *

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=' ')
#     for j in range(i):
#         if(j==0 or i==n-1):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     for j in range(i+1):
#         if(i==n-1 or j==i):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

#         *
#       *   *
#     *       *
#   *           *
# *               *
#   *           *
#     *       *
#       *   *
#         *
#
# n=5
# for i in range(n-1):
#     for j in range(i,n-1):
#         print(" ",end=' ')
#     for j in range(i):
#         if(j==0):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     for j in range(i+1):
#         if(i==j):
#             print('*',end=' ')
#         else:
#             print(" ",end=' ')
#     print()
# for i in range(n):
#     for j in range(i):
#             print(" ",end=' ')
#     for j in range(i,n):
#         if(j==i):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     for j in range(i,n-1):
#         if(j==n-2):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()