data = [1, 2, 3]
for d in data:
    print(d, end=' ')
data[1] = 5
print('-', data[1])

string = 'hello'
for s in string:
    print(s, end=' ')
#string[1] = 'E'
print('-', string[1])

data = (1, 2, 3)
print(data, type(data))
for i in data:
    print(i)
#data[1] = 5

data2 = [i**2 for i in data if i**2 < 5]
print(data2, type(data2))

data3 = []
for i in data:
    if i**2 < 5:
        data3.append(i**2)
print(data3)




# for (int i=0; i <10; i++)
data = [1, 2, 3, 4, 5]
for d in data:
    print(d)

# [1, 5)
data_2d = [[1, 2, 3],
           [4, 5, 6]]
for data in data_2d:
    for d in data:
        print(d, end= ' ')
    print()

# range(1, 10)
# range(1, 10)
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j}')
    print()

# range(1, 11) - 1부터 10까지
# sum, min, max, average = sum / len
print(sum(range(1, 11)))
print(min(range(1, 11)))
print(max(range(1, 11)))
print(sum(range(1, 11))/len(range(1, 11)))

# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ...
# 2 x 1 = 1
# 2 x 2 = 4
# 2 x 3 = 6
# ...
# 9 x 9 = 81

# for idx, d in enumerate(data):
#     print(idx, d)

# a = everything or object
data = [1, 3.14, 'hello', max, range]
for d in data:
    print(d, type(d))
    print('next')

for i in range(len(data)):
    print(data[i], type(data[i]))

pizza_data = ['페페로니', '불고기', '포테이토']
for pizza in pizza_data:
    print(pizza)
print('I do love pizza!')

animal = ['dog', 'cat', 'cow']
for a in animal:
    print(f'{a} 는 정말 훌륭한 반려 동물입니다.')
print('이 동물들은 모두 4개의 다리를 가졌습니다!')

data = range(10)
print(data, type(data))

for d in data:
    print(d, end= ' ')

for d in data:
    print(d, end= ' ')


for i in range(1, 21):
    print(i, end= ' ')

for i in range(1, 21, 2):
    print(i, end=' ')

for i in range(3, 31, 3):
    print(i, end= ' ')

print([i**3 for i in range(1, 11)])

# [1, 11)
data = list(range(1, 11))
# [1, 5)
#print(data, data[1:5], sep='\n')
#print(data, data[:5], data[5:], sep='\n')
print(data, data[::-1], sorted(data, reverse=True), sep='\n')


def swap(a, b):
    temp = a
    a = b
    b = temp
    #a, b = b, a

a, b = 1, 2
print(a, b)
swap(a, b)
print(a, b)

data = (1, 2, 3)
data2 = data.copy()
data = (1, 5, 3)
print(data, data2, sep='\n')

data = list(range(9))
print(data[:3])
print(data[3:6])
print(data[6:])

pizza_data = ('페페로니', '불고기', '포테이토')
new_pizza_list = pizza_data[:]
pizza_data.append('슈프림')
new_pizza_list.append('고르곤졸라')
print(pizza_data)
print(new_pizza_list)