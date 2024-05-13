user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

print(user_0.items())                   # 딕셔너리의 {키:값} 쌍을 items()로 가져옴

for key, value in user_0.items():       # key, value로 딕셔너리 순회
    print(f"\nKey: {key}")
    print(f"Value: {value}")