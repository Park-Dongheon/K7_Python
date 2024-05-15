# 8.5 인수를 임의의 개수로 전달하기

# 함수를 호출할 때 전달되는 인수를 하나로 모으는 매개변수
# 파이썬이 별(*)을 보고 이 함수가 전달받은 인수를 toppings '튜플'에 모음
def make_pizza(*toppings):
    """요청받은 토핑 리스트를 출력합니다"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# print() 루프로 교체
def make_pizza(*toppings):
    """요청받은 토핑 리스트를 출력합니다"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 8.5.1 위치 인수와 임의의 인수 같이 쓰기

# 매개변수 정의 순서: 위치 인수 or 키워드 인수 > 임의의 인수(*args)
def make_pizza(size, *toppings):
    """주문 내용을 요약합니다"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.5.2 임의의 키워드 인수 사용하기

# 여러 가지 종류의 정보를 임의의 인수로 받을때(다양한 인수 타입), 임의의 키-값 쌍을 받도록 키워드 인수를 제한 없이 받음, **kwargs(keyword arguments)
def build_profile(first, last, **user_info):
    """사용자에 대해 아는 정보를 전부 딕셔너리에 저장합니다"""
    user_info['first_name'] = first         # user_info 딕셔너리에 항상 전달받는 이름과 성을 추가
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)


# 연습문제 8-12 / 8-13 / 8-14

# 8-12 샌드위치
def make_sandwich(sandwich, *toppings):
    print("\n")
    sandwich = toppings
    return sandwich

sandwich = ()
sandwich_order = make_sandwich(sandwich, 'sausage')
print(f"주문 받은 샌드위치: {sandwich_order}-Sandwich")
sandwich_order = make_sandwich(sandwich, 'sausage','bulgogi')
print(f"주문 받은 샌드위치: {sandwich_order}-Sandwich")
sandwich_order = make_sandwich(sandwich, 'sausage','bulgogi','chicken')
print(f"주문 받은 샌드위치: {sandwich_order}-Sandwich")

# 8-13 사용자 프로필
def build_profile(first, last, **user_info):
    """사용자에 대해 아는 정보를 전부 딕셔너리에 저장합니다"""
    user_info['first_name'] = first         # user_info 딕셔너리에 항상 전달받는 이름과 성을 추가
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Park', 'Dongheon', location='Busan', field='SW Programmer')
print(user_profile)

# 8-14 자동차
def make_car(manufacturer, model_name, **option_info):
    option_info['manufacturer'] = manufacturer
    option_info['model_name'] = model_name
    return option_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)