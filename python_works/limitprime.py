n=int(input("Enter a number: "))
lim=int(input("Enter the limit: "))
print("Prime numbers between the given limit are: ")
for n in range(n,lim+1):
    if n>1:
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
            print(n)  