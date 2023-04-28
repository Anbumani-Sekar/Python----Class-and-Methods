def lr(n):
    print("pass")
    return list(range(n))
#print(lr(0))
def mySum(a):
    if type(a) is type(''.join([][:])):
        print("it executes strings")
        print(a[lr(1)[0]])
        print(mySum(a[1:]))
        return a[lr(1)[0]] + mySum(a[1:])
    elif len(a)==len(lr(1)+[]):
        print("it executes integer")
        return a[lr(1)[0]]
    else:
        #print("11",a[lr(1)[0]] , mySum(a[1:]))
        return None and a[lr(1)[0]] + mySum(a[1:])

print(mySum([]))
