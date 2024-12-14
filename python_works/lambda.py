# def add(a,b):
#     return a+b
# res=add(10,20)
# print(res)

# x=lambda a,b:a+b
# print(x(10,20))





#factorial lambda

# x=lambda n:1 if n==1 else n*x(n-1)
# print(x(6))





# map: passes every element of an iterable to a function and generate the output of that function.

a=[1,2,34,-4,23,11,45,8,61]
# # def sq(num):
# #     return num**2
# # b=[]
# # for i in a:
# #     b.append(sq(i))
# # print(b)
# b=list(map(sq,a))
# print(b)

b=list(map(lambda num:num**2,a))
print(b)




# filter: passes every element of a iterable to a function, and returns an iterable object consist of of elements that passes a condition.

c=list(filter(lambda num:num%2==0,a))
print(c)



# reduce: pass every iterable into a function and returns a single value.

from functools import reduce
res=reduce(lambda tot,num:tot+num,a)
print(res)