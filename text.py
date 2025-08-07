# Error : when there is a logical or syntax error or system error, memory error in our program, then it is known as error.
# It is a situation when our program is unable to continue its execution due to any certain error.
#
# Exception :  it can be  a situation, where our program stops abruptly due to a logical error, memory error etc.
#
# Exception Handling: it is a mechanism by using which we can handle runtime exceptions. If we use exception handling, then our program will continue to run and perform other operations properly without any fail.
#
# There are mainly few keyword which helps in exception handling
# 1. try :  this block helps in catching the exception. so if there is any code which can produce an exception, then put it inside the try block.
#
# 2. except : it is used to handle the exception in python. if any exception occurs and we are using try block for catching it, then program cursor will automatically be diverted to the except block.
# eg.
# except:
# 	code if error occurs
# except exceptioname:
# 	code if error occurs
#
# 3. finally : finally block is used to execute code in any kind of situations. Usually we put the code inside finally block, which` is compulsory to run in either of the situations. Like whether there is an exception or not.
# eg.
# try:
# 	code
# 	code
# finally:
# 	code
#
# or
# try:
# 	code
# 	code
# except:
# 	code
# 	code
# finally:
# 	code
#
# 4. else
# -Custom exception
# -nested try except block
# -multiple except blocks