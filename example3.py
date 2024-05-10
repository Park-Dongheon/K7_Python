names = ['john', 'bob', 'jane', 'lee', 'kim']

for n in names:
    print(n)

for m in names:
    print('친구의 이름은 : ' + m)

cars = ['tesla', 'bmw', 'benz']
print(f'My favorite car makers are {cars}')
for brand in cars:
    print(f'나는 {brand} 자동차를 갖고싶습니다.')
print('\n')    

invite = ['kim', 'lee', 'park', 'hong']
print(invite)
def printV():
    for i in invite:
        print(f'{i}을 초대합니다.')
    print('\n')    
nonappearance = 'kim'
invite.remove(nonappearance)
print(f'{nonappearance.title()}은 참가하지 못한 손님')
invite.insert(0, 'han')
print(invite)
printV()
invite.insert(0, 'mun')
invite.insert(3, 'choi')
invite.append('myong')
printV()

