# print('hello, world!')

# age = 5
# pi = 3.14
# msg = 'hello, world!'
# data = [1, 2, 3]
# mask = 'everything' or 'object'
# print(type(age), type(pi), type(msg), type(data), type(mask))

# def calc(a, b):
#     print(a + b)
#     print(a - b)
#     print(a * b)
#     print(a / b)
#     print(a // b)
#     print(a ** b)

# a = 3.14
# b = 1.2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a ** b)

# a = 3
# b = 2
# calc(a,b)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a ** b)

# a = 3.14
# b = 1_000_000_000
# print(a, b)
# # calc(a, b)

# a = 5
# b = 3
# print(a, b)
# b, a = a, b
# print(a, b)

# a, b = map(int, input().split())
# b, a = a, b
# print(a, b)

# swap
# temp = a 
# a = b
# b = temp
# print(a, b)

# PI = 3.14
# PI = 3.15
# print(PI)

# msg = "hello, world!"
# print(msg, type(msg))
# print(msg.find('l'))

# print(msg[0:2])
# print(msg[1])
# msg[0] = 'H'    // 값을 못바꿈
# print(msg)
# msg = 'Hello, world!'
# print(msg)

a = 'hello'
b = 'world'

def add(a, b):
    return a + b
print(f'{a},{b},{add(1, 2)}!\t!\n!')

msg = '     hello    '
print(len(msg))
print(len(msg.lstrip().rstrip()))   # msg를 바꾸고 새로운 것을 리턴
print(type(msg.lstrip()))
print(len(msg))

msg = 'hello, hello\', hello, world!'
print(msg.replace('hello', '').replace(',','').lstrip().rstrip())
print(msg)





