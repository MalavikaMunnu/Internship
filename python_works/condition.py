a=10
b=200
c=3

#if (a>b and a>c):
    print("a is greater")
#elif b>c:
#    print("b is greater")
#else:
#    print("c is greater")

if a>b:
    if a>c:
        print("a is big")
    else:
        print("c is big")
elif b>c:
    print("b is big")
else:
    print("c is big")