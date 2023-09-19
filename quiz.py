test_case = int(input('Test Case: '))

def add(a, b):
    return a+b

for i in range(test_case):
    a, b = map(int, input().split())
    #a, b = (input()).split()
    #a = int(a)
    #b = int(b)
    print('Case #', i+1, ': ', add(a, b))
