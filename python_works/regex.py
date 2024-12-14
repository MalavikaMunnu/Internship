# import re
# txt="apple is red"
# res=re.search("is",txt)
# print(res)



# import re
# txt="rain in spain"
# res=re.search("is",txt)
# res=re.search("^r.*spain$",txt)
# print(res)
    


# import re
# s="The rain in spain"
# regex=re.search("l",s)
# print(regex)




# import re
# s="The rain in spain"
# regex=re.findall("i",s)
# print(regex)




# import re
# s="The rain in spain"
# regex=re.split("i",s)
# print(regex)




# import re
# s="The rain in spain"
# regex=re.sub("rain","*",s)
# print(regex)
# regex=re.finditer("in",s)
# for i in regex:
#     print(i.start())
#     print(i.group)
#     print(i)
# print(regex) 




# import re
# # username=input("Enter username: ")
# password=input("Enter password: ")
# regx=re.search("^a[0-9]*e$",password)                   #*- 0 to any
# if regx:
#     print("Valid Password")
# else:
#     print("Invalid Password")



# import re
# # username=input("Enter username: ")
# password=input("Enter password: ")                      #+ - 1 to any
# regx=re.search("^a[0-9]+e$",password)
# if regx:
#     print("Valid Password")
# else:
#     print("Invalid Password")




# import re
# # username=input("Enter username: ")
# password=input("Enter password: ")                        
# regx=re.search("^a[0-9]?e$",password)                         #? - 0 to 1
# if regx:
#     print("Valid Password")
# else:
#     print("Invalid Password")




# import re
# # username=input("Enter username: ")
# password=input("Enter password: ")
# regx=re.search("^a[0-9]{3}e$",password)                         #specific number of occurances
# if regx:
#     print("Valid Password")
# else:
#     print("Invalid Password")




# import re
# # username=input("Enter username: ")
# password=input("Enter password: ")
# regx=re.search("^a[0-9]{3,5}e$",password)                         #set limit
# if regx:
#     print("Valid Password")
# else:
#     print("Invalid Password")




import re
email=input("Enter email: ")
# password=input("Enter password: ")
regx=re.search("^[a-z0-9._-]+[@][a-z0-9]+[.][a-z]{2,3}$",email)
if regx:
    print("Valid Password")
else:
    print("Invalid Password")
