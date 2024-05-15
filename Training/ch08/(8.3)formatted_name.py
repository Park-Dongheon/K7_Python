# 8.3 반환 값

# 반환 값(return value)-함수가 데이터를 처리하고 값을 반환, 호출한 행에 전달

# 8.3.1 단순한 값 반환하기 - 이름·성 실제 이름 반환 함수

def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    full_name = f"{first_name} {last_name}"                 # 두 변수를 조합하고 사이에 공백을 삽입 full_name에 할당
    return full_name.title()                                # full_name의 값을 첫 글자만 대문자로 바꿔 반환

musician = get_formatted_name('jimi', 'hendrix')            # 반환 값을 할당할 변수(musician) 지정
print(musician)

# 8.3.2 인수를 옵션으로 만들기

# 기본 값 사용 시 인수를 옵션으로 사용

# 중간 이름을 필수 값으로 지정 -> 중간 이름을 옵션으로 변경
# 매개변수 first_name, last_name은 항상 존재 위치 인수로 지정, middle_name은 옵션이므로 마지막 위치, 기본 값을 빈 문자열로 지정
def get_formatted_name(first_name, last_name, middle_name=''): 
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# 8.3.3 딕셔너리 반환하기

# 함수의 반환 값에는 제한이 없으며 리스트나 딕셔너리 같은 복잡한 데이터 구조도 반환
def build_person(first_name, last_name):
    """사람에 대한 정보를 딕셔너리로 반환합니다"""
    person = {'first':first_name, 'last':last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

# 함수 정의에 옵션 매개변수 age를 추가, 기본 값을 특별한 값 None으로 지정, None은 일종의 플레이스홀더(placeholder), 조건 테스트에서 False로 평가
def build_person(first_name, last_name, age=None):
    """사람에 대한 정보를 딕셔너리로 반환합니다"""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age                             # person 딕셔너리에 age를 추가 
    return person
musician = build_person('jimi', 'hendrix', age=27)      # 함수를 호출 시 age의 값을 전달하면 해당 값이 딕셔너리에 저장
print(musician)

# 8.3.4 while 루프와 함수

def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 무한 루프입니다!
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    # 이름과 성을 별도의 프롬프트로 받음, break 문을 사용하여 모든 프롬프트에서 쉽게 루프를 중지 가능
    f_name = input("First name:")
    if f_name == 'q':
        break

    l_name = input("Last name:")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# 연습문제 8-6 / 8-7

# 8-6 도시 이름
def city_country(city_name, country_name):
    city = {'city_name':city_name, 'country_name':country_name}
    return city

city_call = city_country('Santiago', 'Chile')
print(city_call)
city_call = city_country('Seoul', 'South Korea')
print(city_call)
city_call = city_country('Tokyo', 'Japan')
print(city_call)


# 8-7 앨범
def make_album(musician_name, al_title, include_song=None):
    album = {'musician':musician_name, 'title':al_title}
    if include_song:
        album['include_song:'] = include_song
    return album

make_album_call = make_album('Seoul', 'South Korea')
print(make_album_call)
make_album_call = make_album('Tokyo', 'Japan')
print(make_album_call)
make_album_call = make_album('London', 'United Kingdom', include_song=15)
print(make_album_call)

# 8-8 사용자 앨범
def make_album(musician_name, al_title):
    album = {'musician':musician_name, 'title':al_title}
    return album

while True:
    print("\nPlease tell me Album Data")
    print("(enter 'q' at any time to quit)")

    m_name = input("musician_name : ")
    if m_name == 'q':
        break
    
    a_title = input("album_title : ")
    if a_title == 'q':
        break

    album_making = make_album(m_name, a_title)
    print(f"\nMaking album : {album_making}!")
    