#---Global Scope---

# def fun():
#     global a
#     a="apple"
#     print(a)
# fun()
# if True:
#     print(a)
# print(a)





#---Local Scope---

def fun():
    a="apple"
    print(a)
fun()
if True:
    print(a)
print(a)