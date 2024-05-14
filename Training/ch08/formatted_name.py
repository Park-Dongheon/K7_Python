# 8.3 반환 값

# 반환 값(return value)-함수가 데이터를 처리하고 값을 반환, 호출한 행에 전달

# 8.3.1 단순한 값 반환하기 - 이름·성 실제 이름 반환 함수

def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다"""
    full_name = f"{first_name} {last_name}"                 # 두 변수를 조합하고 사이에 공백을 삽입 full_name에 할당
    return full_name.title()                                # full_name의 값을 첫 글자만 대문자로 바꿔 반환

musician = get_formatted_name('jimi', 'hendrix')            # 반환 값을 할당할 변수(musician) 지정
print(musician)
