users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        'job': 'developer',
        'salary': 20000
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'job': 'developer',
        'salary': 20000
        },

    }

for username, user_info in users.items():               # users 딕셔너리안의 username 딕셔너리
    print(f"\nUsername: {username}")
    for k, v in user_info.items():                      # users_info 딕셔너리의 {키:값}을 순회하며 출력
        print(f'key={k}, value={v}')
    full_name = f"{user_info['first']} {user_info['last']}"  # 딕셔너리의 디셔너리 key로 value를 출력
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")