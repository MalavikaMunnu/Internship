# a="malavika"
# wrd=a.split(" ")
# b="aeiou"
# res={}
# for i in a:
#     for i in b:
#         res[i]=+1
# print(res) 



a="apple is red"
count=0
for i in a:
    if i in "aeiou":
        count+=1
print(count)