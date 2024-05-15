# import pizza
# from pizza import make_pizza
# from pizza import make_pizza as mp
# import pizza as p
from pizza import *

import printing_functions as print

import shirt
# from shirt import make_shirt
# from shirt import make_shirt as ms
# import shirt as s
# from shirt import *

# 8.6 함수를 모듈에 저장하기

# 함수의 주요 장점: 메인 프로그램에서 코드 블록을 분리
# 함수를 '모듈'로 별도의 파일에 저장, 이 모듈을 메인 프로그램으로 '임포트(import)'
# import문은 현재 실행 중인 프로그램에서 모듈의 코드를 사용 가능하게 함
# 프로그램의 세부 사항을 가려서 전체적인 흐름에 집중
# 다양한 프로그램에서 함수를 활용 가능
# 다른 프로그래머가 만든 라이브러리도 사용 가능


# 8.6.1 전체 모듈 임포트하기
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.2 특정 함수 임포트하기
# 함수 호출 시 점(.) 표기법 사용x, make_pizza() 함수를 명시적으로 임포트
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.3 as로 함수에 별칭 부여하기
# 임포트할 함수가 기존 함수 이름과 충동하거나, 너무 길면 별칭으로 수정 가능
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.4 as로 모듈에 별칭 부여하기
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 8.6.5 모듈의 함수를 모두 임포트하기
# 점(.) 표기법 사용하지 않고 함수 이름을 바로 호출 가능, 임포트한 모듈의 이름이 같은 함수와 변수를 덮어씀, 필요한 함수만 임포트하거나 점 표기법으로 호출 권장
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# 연습문제 8-15 / 8-16 / 8-17

# 8-15 모델 출력
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print.print_models(unprinted_designs, completed_models)
print.show_completed_models(completed_models)

# 8-16 임포트
shirt.make_shirt('I love Python')

# 8-17 함수 스타일