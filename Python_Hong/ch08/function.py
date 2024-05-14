def greet_user():
    """Display a simple greeting."""                         # 함수의 설명문, 함수를 찾기위한 권장사항
    print("Hello!")
greet_user()
help(greet_user)                                             # 함수의 정의와 body를 보여줌
print(greet_user.__doc__)                                    # 함수에 쓰여있는 독스트링(docstring)을 보여줌

def describe_pet(animal_type, pet_name):                     # 위치 인수 예
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')

def describe_pet(animal_type, pet_name):                     # 키워드 인수 예, 순서가 상관이 없음
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='harry', animal_type='hamster')        # key='value'

def describe_pet(pet_name, animal_type='dog'):               # default parameter: animal_type='dog, 인자값을 지정하지 않을 시 처리
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')

def get_formatted_name(first_name, last_name, middle_name=''): # 호출하는 인자값 개수에 따라 조건문에서 반환
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')               # musician의 리턴 값이 string임을 유추
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name, age=None):             # 딕셔너리 타입 person을 반환
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)             # musician은 딕셔너리 타입
print(musician)

def greet_users(names):                                        # 리스트의 각원소에 대해서 for문으로 출력
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']                         # 리스트 형태 인자 전달
greet_users(usernames)

def print_models(unprinted_designs, completed_models):         # 함수의 parameter의 type을 알 수 없음
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:                                   # list가 empty가 아니면 true
        current_design = unprinted_designs.pop()               # list의 마지막 요소를 하나씩 out
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
### main 프로그램부터 봐야 한다
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# print_models(unprinted_designs, completed_models)
# print(f'원래 변수 출력 = {unprinted_designs}')
# print(f'수정 여부 출력 = {completed_models}')                    # 함수 print_models에 의해 수정
# show_completed_models(completed_models)

print_models(unprinted_designs[:], completed_models)            # [:]사본을 만들어 함수에 전달 
print(f'원래 변수 출력 = {unprinted_designs}')
print(f'수정 여부 출력 = {completed_models}')
show_completed_models(completed_models)

# *toppings 변수는 임의의 갯수 parameter => tuple에 모음
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for t in toppings:                # t는 각각의 toppings의 튜플
        print(f"- {t}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):         # **를 사용하면 dictionary
    """Build a dictionary containing everything we know about a user."""
    # user_info 딕셔너리에 key:value 두 개(first_name, last_name) 추가
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',# build_profile() 함수는 딕셔너리를 반환
                             location='princeton',# 3번째 argument부터 key=value로 전달
                             field='physics')
print(user_profile)

