# class Student:
#     def __init__(self,name,rno,clss):
#         #instance variable
#         self.Name=name
#         self.Rollno=rno
#         self.Class=clss
#     #class variable
#     center="Calicut"
# ob=Student("Chottu",12,"BCA")
# print(ob.Name)

# oc=Student("Ash",13,"BSc Cs")
# print(oc.Name)






class Student:
    def __init__(self,name,rno,clss):
        print(self)
        self.Name=name
        self.Rollno=rno
        self.Class=clss
    center="Calicut"
    def display(self):
        print(self.Name)
ob=Student("Chottu",12,"BCA")
ob.display()
# print(ob)
# print(ob.Name)
# print(ob.center)

oc=Student("Ash",13,"BSc Cs")
oc.display()
# print(oc)
# print(oc.Name)
# print(oc.center)