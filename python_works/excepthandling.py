# try:
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     res=a/b
#     print(res)
# except:
#     print("Error occurred!!")
# finally:
#     print("Program ended!!")






# try:
#     a=int(input("Enter first number: "))
#     b=int(input("Enter second number: "))
#     res=a/b
#     print(res)
# except ValueError:
#     print("Value Error occurred!!")
# except ZeroDivisionError:
#     print("Error bcz of division by zero!!")
# else:
#     print("No exceptions!!")
# finally:
#     print("Program ended!!")





try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    res=a/b
    print(res)
except ValueError as msg:
    print(msg)
except ZeroDivisionError as msg:
    print("Error bcz of division by zero!!")
else:
    print("No exceptions!!")
finally:
    print("Program ended!!")
