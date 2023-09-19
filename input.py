a = int(input("input 1st number: "))
b = int(input("input 2st number: "))
c = input("input operator(+, *): ")

#print(a+b)
#print("%d + %d = %d" % (a, b, a+b))
#print("%s + %s = %s" % (a, b, a+b))

def add(a, b):
    return a + b

def multi(a, b):
    return a * b

if c == '+':
    result = add(a, b)
    print(result)
elif c == '*':
    result = multi(a, b)
    print(result)
else:
    pass


