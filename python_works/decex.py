def wrapper(fn):
    def inner(a,b):
        if a>b:
            return fn(a,b)
        else:
            return fn(a,b)
    return inner

@wrapper
def sub(a,b):
    return a-b

@wrapper
def div(a,b):
    return a/b

d=div(200,20)
s=sub(20,5)

print(d)
print(s)