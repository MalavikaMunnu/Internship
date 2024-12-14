from dbconn import addcontact,viewcontacts

flag=0
while flag==0:
    op=input("1. Add Contacts\n2. View Contacts\n3. Exit\n=> ")
    if op=='1':
        nm=input("Enter name: ")
        pn=input("Enter phonenumber: ")
        res=addcontact(nm,pn)
        if res==1:
            print("Contact added successfully!!")
        else:
            print("Contact cannot be added!!")
    if op=='2':
        phonebook=viewcontacts()
        # print(phonebook)
        for i in phonebook:
            print(i)
    if op=='3':
        flag=0