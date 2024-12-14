num=[1,2,1,1,2,3,2,1,3,4,56,4,3,2,1,56]
# a=[]
# for i in num:
#     if i not in a:
#         a.append(i)
# print(a)

c=0
for i in num:
    if i%2!=0:
        c+=1
print(c)