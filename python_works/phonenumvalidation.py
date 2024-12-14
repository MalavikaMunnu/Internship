import re
phone=input("Enter phone: ")
regx=re.search("^[+]91-[0-9]{10}$",phone)
if regx:
    print("Valid Contact")
else:
    print("Invalid Contact")
 