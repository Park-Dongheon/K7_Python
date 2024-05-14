## immutable 객체 - str, int
def modify_string(s):
    s = s + "world"         ## 함수 내에서 매개변수 값을 처리 가능
    print(f"함수내 출력={s}")
st = "hello"
## string을 전달하므로 immutable객체, 새로운 문자열 객체를 복사해서 매개변수에 전달
modify_string(st)   
print(st)


def modify_number(number):
    number = number + 10
    print(f"함수내 출력={number}")
num = 10
modify_number(num)
print(f"함수 종료후 출력= {num}")

## 함수를 모듈(module)이라는 별도의 파일에 저장, 메인 프로그램으로 모듈(function)임포트(import)
import function 
function.make_pizza(16, 'pepperoni')
function.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

## 모듈에서 특정 함수만 임포트
from function import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

## 특정 함수의 이름을 수정-타이핑 간소화
from function import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushroom', 'green peppers', 'extra cheese')

import function as f
f.make_pizza(16, 'pepperoni')
f.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

### 파이썬 람다함수 설명 및 예제 - 교재 누락
### 문법 형태 ------- 함수명 = lambda 매개변수 : 표현식
### map(함수, 리스트 or 튜플)-람다 표현 수정 => map((lambda 매개변수:표현식), 리스트 or 튜플)
### filter(함수, 리스트 or 튜플)-람다 표현 수정 => filter((lambda 매개변수:표현식), 리스트 or 튜플)
### filter 함수의 첫번째 인자가 True 인 경우의 값만 가지고와서 리스트

# 람다식코드
## part.1
def ten_times(func):    # ten_times 함수에서 매개변수 func
    for i in range(5):
        func()
def print_hello():
    print("hello")
ten_times(print_hello)  # ten_times를 호출하면서 argument로 print_hello 함수를 전다
## part.2
def add(x, y):
    return x + y
def apply_operation(operation, x,y):    
    return operation(x, y)
result = apply_operation(add, 3, 4)     # add함수 argument로 operation 매개변수로 전달
## part.3
def power(item):
    return item**2
def under_three(item):
    return item < 3
lst = [1, 2, 3, 4, 5]
map_list = map(power, lst) 
print(list(map_list))
filter_list = filter(under_three, lst)
print(list(filter_list))
## part.4
m_list = map(lambda x : x*x, lst)      # part.3의 power 함수의 람다식 표현
print(list(m_list))