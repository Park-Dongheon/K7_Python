score = 70


if (90 <= score) and (score < 100):
    print('A')
elif (80 <= score) and (score < 90):
    print('B')
else:
    print('F')

a = 5
if a == 5:
    print('right!')

msg = 'hello'
if msg == 'hello':
    print('right!')

data = [1, 2, 3]
if data == [1, 2, 3]:
    print('right!')

if []:
    print('right!!!')

data = [1, 2, 3]
if 4 in data:
    print('Here!')

string = 'hello'
if 'e' in string:
    print('Here!')




score = 100

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
#     print('right------')

msg = 'hello'
if msg == 'hello':
    print('right!')

data = [1, 2, 3]
if data == [1, 2, 3]:
    print('right!')

if []:
    print('right!!!')

data = [1, 2, 3]
if 4 in data:
    print('Here!')

string = 'hello'
print(string.upper())
if 'e' in string:
    print('Here!')

a = 15
if a < 5 or a > 10:
    print('a')

#  A B  AND OR
#  0 0  0    0
#  0 1  0    1
#  1 0  0    1
#  1 1  1    1

car = 'kia'
if car == 'audi':
    print("Is car == 'audi? I predict True.")
elif car.lower() == 'audi':
    print("Is car == 'audi? I predict True.")
else:
    print(car == 'kia')

a = 6
if a == 5:
    print('the same')
elif a < 5:
    print('less than 5')
elif a > 5:
    print('more than 5')



data = [1, 2, 3]
if 2 in data:
    print('there is 2!')
if not 4 in data:
    print('there is not 4!')

print(1 + 2)
print(1 < 2)
print(sum([True, True, True]))

alien = 'red'
alien_color = ['green', 'yellow', 'red']

if alien == 'green':
    print('get 5 points!')
#else:
#    print('get 10 points!')    

if alien == 'green':
    print('get 5 points!')

alien = 'red'
if alien != 'green':
    print('get 10 points!')  

if alien == 'green':
    print('get 5 points!')
elif alien == 'yellow':
    print('get 10 points')
elif alien == 'red':
    print('get 15 points')
else:
    print('get 10 points!')  

age = 1

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
elif 65 <= age:
    print('elder')

data = [1, 2, 3]
for d in data:
    if d < 2:
        print(d)
    else:
        print('wrong!')

if []:
    print('hahahahah!')

names = ['kim', 'lee', 'park', 'choi', 'oh', 'admin']

for name in names:
    if name == 'admin':
        print('Hello, Admin!')
    else:
        print('Hello, Member, again!')

names = ['kim', 'lee', 'park', 'choi', 'oh', 'admin']

names = []

if not names:
    print('There is no member!')

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