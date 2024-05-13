# 8.1 함수 정의하기 - 인사말 출력

# 함수정의(function definition) 키워드 def, ()안에 함수가 받는 정보 정의, def greet_user(): 다음 함수 바디(body)
def greet_user():
    # 독스트링(docstring)-함수가 수행하는 작업을 설명
    """단순한 인사말을 표시합니다"""
    print("Hello!")
#함수호출(function call)-파이썬에게 함수의 코드를 실행하도록 지시 
greet_user()

# 8.1.1 함수에 정보 전달하기 / 8.1.2 인수와 매개변수

# username에 지정한 값을 받음, 함수를 호출할 때마다 username에 해당하는 값을 예상, username-함수가 동작하기 위해 필요한 정보 == 매개변수(parameter)
def greet_user(username):
    """단순한 인사말을 표시합니다"""
    print(f"Hello, {username.title()}!")
# 호출할 때 'jesse' 전달, 인수(argument)-함수를 호출할 때 함수로 전달되는 정보
greet_user('jesse')

# 연습문제 8-1 / 8-2

# 8-1 메시지
def display_message():
    print("함수 정의하기")

display_message()

# 8-2 좋아하는 책
def favorite_book(title):
    print(f"내가 가장 좋아하는 책은 {title}입니다")

favorite_book("이상한 나라의 앨리스")