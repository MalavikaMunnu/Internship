a=int(input("Enter a number:"))
temp=a
d=0
while a>0:
    c=a%10
    d=d+(c**3)
    a=a//10
print("res",d)
if temp==d:
    print(temp,"is an Armstrong number")
else:
    print(temp,"is not an Armstrong number")