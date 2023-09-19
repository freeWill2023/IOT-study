a = int(input("input 1st number: "))
b = int(input("input 2st number: "))
c = input("input operator(+, *): ")

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


