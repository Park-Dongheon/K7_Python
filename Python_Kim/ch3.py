data = [1, 2, 3, 3, 3]
print(data, type(data))

# data = list()        # 자바의 클래스 객체 생성과 비슷한 문법
# print(data, type(data))

print(data[0])
print(data[1])
print(data[2])
print(len(data))

data.append(6)
data.append(7)
data.append(8)
print(data)
print(len(data))

data[3] = 4
data[4] = 5
print(data, len(data), sum(data), min(data), max(data))

data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
data = list(range(10, 0, -1))
print(data, type(data), sorted(data))

# 10
# 10 9 8 7 6 5 4 3 2 1 
# 합계를 구하시오!, 정렬하시오!, 최댓값을 찾으시오!, 최솟값을 찾으시오!

# data = input() -- 객체 생성형
# data = input().split() -- list
## input을 string타입으로 split
# data = list(map(int, input().split()))
# print(data, type(data), type(data[0]))
# # print(sum(data.split()))
# print(sum(data))

number = int('56')
print(number, type(number))

data =[1, 2, 3]
del data[1]
print(data)

# data 리스트 안의 모든 값을 Object로 본다
data = [1, 2, 3.14, 'hello', len, range(5)]
print(data)
for d in data:
    print(data, type(data))

# data 리스트 출력
data = [1, 2, 3, 4, 5]
print(data[len(data)-1])

data.reverse()
print(data)

print(data[::-1])


msg = 'age'
print(msg == msg[::-1])

# 수정 제거 추가
data.append(1)
print(data)

data.pop()
print(data)

data.insert(1, 1)
print(data)

del data[1]
print(data)

data.remove(1)
print(data)

print(sorted(data))     # sorted는 리스트 객체를 임시로 받아서 정렬
print(data)

data.sort()
print(data)


