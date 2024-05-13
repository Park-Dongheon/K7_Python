print('hello, world!')

age = 5;
pi = 3.14
msg = 'hello, world!'
data = [1, 2, 3]
mask = 'everything' or 'object'
print(type(age), type(pi), type(msg), type(data), type(mask))



def calc(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a ** b)

a=2
b=4
calc(a, b)

a=3.14
b=1.2
calc(a, b)

a = 3.14
b = 1
calc(a, b)


msg = 'hello, world!'
print(msg)

print(msg[0])
print(msg[1])
# msg[0] = 'H'
# print(msg)

a = 'hello'
b = 'world'

def add(a, b):
    return a+b
print(f'{a}, {b}, {add(1, 2)}! hahahaha!')
