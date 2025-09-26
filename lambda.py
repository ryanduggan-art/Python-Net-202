# lambda

x = lambda a: a + 10
print(x(5))

x = lambda a, b: a * b
print(x(5,6))

x = lambda a,b,c: a + b + c
print(x(5, 6, 2))

def myFunction(n):
    return lambda a: a*n

    mydoubler = myFunction(2)
    mytripler = myFunction(3)

    print(mydoubler(11))
    print(mytripler(11))
