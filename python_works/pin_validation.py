pin=input("Enter pin: ")
for i in pin:
    if i.isalpha():
        print("not valid")
        break
else:    
    if len(pin)==4 or len(pin)==6:
        for i in pin:
            if int(i)%2==0:
                print("not valid")
                break
            else:
                print("valid")
        else:
            print("not valid") 