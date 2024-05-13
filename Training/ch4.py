# data = [1, 2, 3]
# for d in data:
#     print(d, end=' ')
# data[1] = 5
# print('-', d[1])
# string = 'hello'
# for s in string:
#     print(s, end=' ')
# string[1] = 'E'
# print('-', string[1])
# string 타입은 변경 불가

# 튜플, 값 수정 불가
# data = (1, 2, 3)
# for i in data:
#     print(i)

# data[1] = 5
# for()문 4 줄 = 2줄 줄이기
# data2 = [i**2 for i in data if i**2 < 5]
# print(data2, type(data2))

# data3 = []
# for i in data:
#     if i**2 < 5:
#         data3.append(i**2)
# print(data3)

# for(int i = 0; i < 10; i++), for()문 ->
#-> for(item : array)
# data = [1, 2, 3, 4, 5]
# for d in data:
#     print(d)

# range(시작위치, 마지막위치전, 데이터의 단계), '_' 반복만 원할경우
# data_2d = [[1, 2, 3],
#            [4, 5, 6]]
# for i in range(10):
#     print('a', end=' ')
# for i in range(10):
#     print('a', end=' ')
#     print(i, end=' ')
#     for d in data:
#         print(d)

# 구구단 - range(1, 10)
# 1 * 1 = 1
# 1 * 2 = 1
# 1 * 3 = 1
# ...
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i * j}')
#     print()

# enumeratr() 반복문은 index와 value 둘다 출력
# for idx, d in enumerate(data):
#     print(idx, d)

# a = everything or object
# data = [1, 3.14, 'hello', max, range]
# for d in data:
#     print(d, type(d))
#     print('next')

# for i in range(len(data)):
#     print(data[i], type(data[i]))

# range(1, 11) - 1부터 10까지
# sum, min, max, average
# print(sum(range(1, 11)))
# print(min(range(1, 11)))
# print(max(range(1, 11)))
# print(sum(range(1, 11))/ len(range(1, 11)))

# 연습문제
# pizza_data = ['페페로니', '불고기', '포테이토']
# for pizza in pizza_data:
#     print(pizza)
# print("I do love pizza!")

# animal = ['dog', 'cat', 'cow']
# for a in animal:
#     print(f'{a}는 반려동물 입니다.')
# print('이 동물들은 모두 4개의 다리르 가졌습니다.')

# data = range(2, 1001, 2)
# print(data, type(data))
# for d in data:
#     print(d, end=' ')

# 연습문제
# for i in range(1, 21):
#     print(i, end=' ')

# data = list(range(1, 1000001))
# for d in data:
#     print(d, end=' ')

# print(min(data))
# print(max(data))
# print(sum(data))

# data = list(range(1, 1000001, 2))
# for d in data:
#     print(d, end=' ')

# for d in range(3, 31, 3):
#     print(d, end=' ')

# print([i ** 3 for i in range(1, 11)])

# 4.4 슬라이싱
# [리스트 시작위치 : 리스트 마지막위치 : 리스트 단계]
data = list(range(1, 11))
# [1, 5]
# print(data[1:5])
# print(data, data[1:5], sep='\n')
# print(data, data[:5], data[5:], sep='\n')
# print(data, data[::1], sorted(data, reverse=True), sep='\n')

# def swap(a, b):
#     temp = a
#     a = b
#     b = temp
#     return a, b
#     # a, b = b, a

# a, b = 1, 2
# print(a, b)
# a, b = swap(a, b)
# print(a, b)

# data = [1, 2, 3, []]
# # 인덱스를 모두 생략하는 슬라이스([:]) 문법으로 리스트 복사(리스트 사본)
# data2 = data[:]
# # data2 = data.copy()
# data2[1] = 5
# print(data, data2, sep='\n')

# 연습문제
my_foods = ['pizza', 'falafel', 'carrot cake', 'bulgogi', 'potato']
print(f'리스트의 첫 세 항목은: {my_foods[:]}')
print(f'리스트의 중간 세 항목은: {my_foods[1:4]}')
print(f'리스트의 마지막 세 항목은: {my_foods[:3]}')


