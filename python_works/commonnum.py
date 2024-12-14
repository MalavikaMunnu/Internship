a=[1,2,3,4,44,56,7,90]
b=[2,3,44,19,82,90,7]
c=[]
# for i in a:
#     for j in b:
#         if i==j:
#             c.append(i)
# print(c)


for i in a:
    if i in b:
        c.append(i)
print(c)        