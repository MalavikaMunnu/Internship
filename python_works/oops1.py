# class Student:
#     name="Chottu"
#     roll_no=103
#     course="BCA"
#     def fun(self):
#         print("Hello")
# ob=Student()
# print(ob)
# print(ob.name)
# print(ob.roll_no)
# print(ob.course)
# ob.fun()



class Student:                                        #default constructor
    def __init__(self):
        print("Object created")
    name="Chottu"
    roll_no=103
    course="BCA"
    def fun(self):
        print("Hello")

ob=Student()

oc=Student()