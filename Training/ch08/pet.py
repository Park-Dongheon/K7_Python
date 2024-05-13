# 8.2 인수 전달하기

# 매개변수를 여러 개 정의할 수 있는 것처럼, 함수 호출할 때도 인수를 여러개 전달 가능
# 위치 인수(positional argument)-매개변수와 똑같은 순서로 인수 전달, 키워드 인수(keyword argument)-변수 이름과 값을 인수로 함께 전달·순서 상관 없음

# 8.2.1 위치 인수

def describe_pet(animal_type, pet_name):                # 함수가 반려동물의 종류와 이름을 받게 정의
    """반려동물 정보를 표시합니다"""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')                # 함수 호출 시 hamster 인수는 animal_type 매개변수, harry 인수는 pet_name에 할당
describe_pet('dog', 'willie')

# 8.2.2 키워드 인수 - 함수에 전달하는 이름-값 쌍

def describe_pet(animal_type, pet_name):
    """반려동물 정보를 표시합니다"""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
# 두 함수 호출이 동일
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# 8.2.3 기본 값

# 함수 정의 시 각 매개변수의 기본 값(default value)을 지정 가능
# 함수 호출 시 매개변수에 대응하는 인수 존재 시 파이썬은 그 값을 사용, 매개변수의 기본 값 지정하면 함수 호출 시 인수 없어도됨
# animal_type의 기본 값을 dog로 지정, pet_name을 위치 인수로 해석
# 기본 값이 있는 매개변수는 반드시 기본 값이 없는 매개변수보다 뒤에 정의, 파이썬이 위치 인수를 정확히 해석 할 수 있음
def describe_pet(pet_name, animal_type='dog'):
    """반려동물 정보를 표시합니다"""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
# animal_type을 지정하지 않고 호출해도 기본 값으로 실행 후 값 반환
describe_pet(pet_name='willie')

# 8.2.4 동등한 함수 호출하기

# 매개변수 pet_name에 할당될 인수는 필수 위치·키워드 전달, 매개변수 animal_type에 인수 할당할 시 위치·키워드 전달
# 다음 호출은 모두 동일

# 개 윌리
describe_pet(pet_name='willie')
describe_pet('willie')

# 햄스터 해리
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# 8.2.5 인수 에러 피하기

# 매개변수 숫자와 인수 숫자가 일치하지 않으면 에러
# describe_pet()              # 트레이스백 표시(찾은 문제 위치 -> 잘못된 함수 호출 -> 함수 호출할 때 인수 누락했음 보여줌)

# 연습문제 8-3 / 8-4 / 8-5

# 8-3 티셔츠
def make_shirt(shirt_size, shirt_msg):
    print(f"\nT-shirt size: {shirt_size} Tshirt message: {shirt_msg}")

make_shirt('Small', 'Software Developer')
make_shirt(shirt_size='Small', shirt_msg='Software Developer')

# 8-4 라지 셔츠
def make_shirt(shirt_msg, shirt_size='Large', shirt_sie='Midium'):
    print(f"\nT-shirt size: {shirt_size} Tshirt message: {shirt_msg}")

make_shirt('I love Python')

# 8-5 도시
def describe_city(contry_name, city_name="레이캬비크"):
    print(f"\n{city_name}는 {contry_name}에 있습니다.")

describe_city('South Korea',city_name='Seoul')
describe_city(contry_name='Japan',city_name='Tokyo')
describe_city('Iceland')
