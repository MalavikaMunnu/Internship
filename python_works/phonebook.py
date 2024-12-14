phonebook={ "nazri":{"name":"nazri","phone":"876543219","email":"nazri@1234"} }


def fun():
    new={}
    name=input("Enter name: ")
    phone=int(input("Enter number: "))
    email=input("Enter email: ")
    new.update({"name":name})
    new.update({"phone":phone})
    new.update({"email":email})
    phonebook.update({name:new})
    print(phonebook)
flag=0
while flag==0:
    op=int(input("1. Add\n2. View\n3. Update\n4. Delete\n5. Exit"))
    if op==1:
        fun()
    if op==2:
        print(phonebook)
        ve=input("Enter name: ")
        for i in phonebook:
            if i in ve:
                print(phonebook[i])
    if op==3:
        address=input("Enter address: ")
        phonebook.update({"address":address})
    if op==4:
        del(phonebook)
        print(phonebook)
    if op==5:
        flag=0