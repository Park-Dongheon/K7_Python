score = 100
# if 90 < score < 100:
#     print('A')
if (90 <= score) and (score <= 100):
    print('A')
elif (80 <= score) and (score < 90):
    print('B')
else:
    print('F')


a = 5
if a == 5:
    print('right!')

# a = 3.14
# if a == 3.14:
#     print('right-------')

msg = 'hello'
if msg == 'hello':
    print('right!!')

data = [1, 2, 3]
# data = []
if data == [1, 2, 3]:
    print('right!!!')

if []:
    print('right!!!')

data = [1, 2, 3]
if 3 in data:
    print('Here!')

string = 'hello'
if 'e' in string:
    print('Here!!')

string = 'hello'
print(string.lower())
if 'e' in string:
    print('Here!')

msg1 = 'hello'
msg2 = 'Hello'
print( msg1 > msg2 )

a = 15
if not(a < 5 or a > 10):
    print('a')

# A B AND OR
# 0 0  0  0
# 0 1  0  1
# 1 0  0  1
# 1 1  1  1

# 연습문제
car = 'subaru'
print("Is cat == 'subaru' ? I predict True.")
print(car == 'subaru')

print(car == 'audi')

if car == 'audi':
    print("\n Is car == 'audi' ? I predict True.")
    
if a > 5:
    print('a')

if 'r' in car:
    print('I predict True.')
car = 'SuBaru'
print(car.lower())
if 'B' in car:
    print('I predict False.')

print(1 + 2)
print(1 < 2)
print(sum([True, True, True]))         # 2

# 0: false, 나머지 숫자: true
if 1 < 2:
    print('aaa')

# 연습문제
alien = 'green'
alien_color = ['green', 'yellow', 'red']
if alien == 'green':
    print('플레이어가 5점을 획득')
elif alien == 'yellow':
    print('플레이어가 10점을 획득')
elif alien == 'red':
    print('플레이어가 15점을 획득')
else:
    print('플레이어가 점수를 획득하지 못했습니다.')

if alien != 'green':
    print('플레이어가 10점을 획득')
else:
    print('플레이어가 점수를 획득하지 못했습니다.')

age = 32
if age < 2:
    print('baby')
elif age < 4:
    print('toddler')
elif age < 13:
    print('kid')
elif age < 20:
    print('teenager')
elif age < 65:
    print('adult')
else:
    print('elder')

data = [1, 2, 3]
for d in data:
    if d < 2:
        print(d)
    else:
        print('wrong!')

# 연습문제
names = ['kim', 'lee', 'park', 'choi', 'oh', 'admin']
for name in names:
    if name == 'admin':
        print('관리자님 안녕하세요. 상태 보고서를 보시겠습니까?')
    else:
        print(f'{name} 님 안녕하세요. 다시 로그인해 주셔서 감사합니다.')

names2 = names[:]
name2 = []
if not names2:
    print('사용자가 있어야 합니다.')

user_ids = ['kim', 'LEE', 'park', 'choi', 'oh', 'admin']
new_ids = ['alice', 'bob', 'kim', 'Lee']
for id in new_ids:
    if id in user_ids:
        print(f'There is a member with id {id}!')
    else:
        print(f'{id} is available!')

user_ids_lower = [id.lower() for id in user_ids]
for id in new_ids:
    if id.lower() in user_ids_lower:
        print(f'There is a member with id {id}!')
    else:
        print(f'{id} is available!')
