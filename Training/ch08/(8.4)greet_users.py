# 8.4 함수에 리스트 전달하기

# 이름, 숫자, 딕셔너리 등의 리스트를 함수에 전달, 함수가 리스트의 내용에 직접 접근 가능

def greet_users(names):
    """리스트의 사용자에게 단순한 인사말을 출력합니다"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

# 리스트는 함수 외부에서 정의, greet_users() 함수를 호출하면서 username 리스트를 전달
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# 8.4.1 함수 내부에서 리스트 수정하기

# 출력할 디자인이 저장된 리스트
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 남은 게 없으 때까지 디자인을 출력합니다
# 출력한 디자인을 completed_models로 옮깁니다
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing models: {current_design}")
    completed_models.append(current_design)

# 완료된 디자인을 표시합니다
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# 출력할 디자인 리스트: unprinted_designs, 출력이 끝난 디자인: completed_models
# unprinted_designs에 디자인이 남아있는 한, while 루프는 리스트 마지막의 디자인을 꺼내 current_design에 저장, 현재 디자인을 출력하고 있다는 메시지를 표시
# completed_models 리스트로 디자인을 옮긴 후 출력

# 독립된 작업 수행하는 함수 두 개로 만들기 - 더 쉬운 코드 체계화,확장·유지 관리 
def print_models(unprinted_designs, completed_models):
    """
    남은게 없을 때까지 디자인을 출력합니다
    출력이 끝난 디자인을 completed_models 리스트로 이동합니다
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """출력된 모델을 모두 표시합니다"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
show_completed_models(unprinted_designs)        # 빈 리스트


# 8.4.2 함수가 리스트를 수정하지 못하게 하기

def print_models(unprinted_designs, completed_models):
    """
    남은게 없을 때까지 디자인을 출력합니다
    출력이 끝난 디자인을 completed_models 리스트로 이동합니다
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """출력된 모델을 모두 표시합니다"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
show_completed_models(unprinted_designs)        # unprinted_designs 원본 리스트 원소 출력


# 연습문제 8-9 / 8-10 / 8-11

# 8-9 메시지
def show_messages(messages):
    print("\n")
    while messages:
        message = messages.pop()
        print(f"Message: {message}")

messages = ['k-ditital-7', 'park-dongheon', 'software programmer']
show_messages(messages)

# 8-10 메시지 전송
def show_messages(messages, sent_messages):
    print("\n")
    while messages:
        message = messages.pop()
        print(f"Message: {message}")
        sent_messages.append(message)

def send_messages(sent_messages):
    for copy_message in sent_messages:
        print(f"Copy_Message: {copy_message}")

messages = ['k-ditital-7', 'park-dongheon', 'software programmer']
sent_messages = []
show_messages(messages, sent_messages)
send_messages(sent_messages)

# 8-11 보관된 메시지
def show_messages(messages, sent_messages):
    print("\n")
    while messages:
        message = messages.pop()
        print(f"Message: {message}")
        sent_messages.append(message)

def send_messages(sent_messages):
    for copy_message in sent_messages:
        print(f"Copy_Message: {copy_message}")

messages = ['k-ditital-7', 'park-dongheon', 'software programmer']
sent_messages = []
show_messages(messages[:], sent_messages)
send_messages(sent_messages[::-1])
for message in messages:
    print(f"원본 메시지: {message}")
