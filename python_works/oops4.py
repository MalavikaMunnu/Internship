# class A:        #parent class/super class
#     name="Name is A"
#     def fun(self):
#         print("Method of A")
# class B(A):     #child class/sub class
#     pass
# b=B()
# print(b.name)
# b.fun()




# --- Single Inheritance ---
# class A:
#     name="Name is A"
#     def fun(self):
#         print("Method of A")
# class B(A):
#     def display(self):
#         print(super().name)
#         super().fun()
# b=B()
# b.display()




# --- Multiple Inheritance --- 
# class A:
#     name="Name is A"
#     def fun(self):
#         print("Method of A")
# class B:
#     place="Kkd"
#     def display(self):
#         print("Hi Child !!")
# class C(A,B):
#     pass
# c=C()
# print(c.name)
# print(c.place)
# c.fun()





# # --- Multilevel Inheritance ---
# class A:
#     name="A"
#     def fun(self):
#         print("Method of A")
# class B(A):
#     pass
# class C(B):
#     pass
# c=C()
# print(c.name)
# c.fun()



# ---Heirarchical Inheritance ---
# class A:
#     name="A"
#     def fun(self):
#         print("Method of A")
# class B(A):
#     pass
# class C(A):
#     pass
# b=B()
# print("B",b.name)
# b.fun()

# c=C()
# print("C",c.name)
# c.fun()




# --- Hybrid Inheritance ---
class A:
    def fun1(self):
        print("Method of A")
class B(A):
    def fun2(self):
        print("Hey B!!")
class C(A):
    def fun3(self):
        print("Chill C!!")
class D(B,A):
    def fun4(self):
        print("Dude D!!")
d=D()
d.fun1()
d.fun2()
d.fun4()