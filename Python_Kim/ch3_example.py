names = ['kim', 'lee', 'park']
print(names[0])
print(names[1])
print(names[2])

for name in names:
    print(f'hello, {name}')

cars = ['telsa', 'bmw', 'benz']    
print(f'My favorite car makers are {cars}')

names = ['kim', 'lee', 'park']
print(names[0])
print(names[1])
print(names[2])

for name in names[:2]:
    print(f'invite, {name}')
print()

print(names[2])
names[2] = 'son'
print(names)

for name in names:
    print(f'invite, {name}')
print()

names.insert(0, 'choi')
names.insert(2, 'jo')
names.append('ryu')

for name in names:
    print(f'invite, {name}')
print('names', names)


while 2 < len(names)  :
    names.pop()

print(names, len(names))

for name in names:
    print(f'invite, {name}')
print()


del names[0]
del names[0]
print(names)


cities = ['seoul', 'jeju', 'osaka', 'tokyo', 'newyork']
print('before', cities)
print(sorted(cities))
print('after', cities)
print(sorted(cities, reverse=True))
print(cities)
cities.reverse()
print('reverse', cities)
cities.reverse()
print('reverse', cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)

print(len(cities))
print(cities[6])