a=int(input("Enter a number:"))
count=0
while a>0:
    c=a%10
    a=a//10
    count+=1
print(count)
    