# Write a progran to find biggest word in a string

# a=input("Enter a sentence: ")
# b=a.split(" ")
# print(b)
# l=0
# res=""
# for i in b:
#     if l<len(i):
#         l=len(i)
#         res=i
# print(res)






# Write a program to find a given number is valid or not. Add valid phone numbers into "Phone_numbers.txt"

import re
phone=input("Enter phone: ")
b=re.search("^[0-9]{10}$",phone)
if b:
    print("Valid Contact")
    f=open("Phone_number.txt","a")
    c=f.writelines(phone)
    c=f.writelines("\n")
else:
    print("Invalid Contact")
