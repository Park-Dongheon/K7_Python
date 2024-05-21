from pathlib import Path
import os
###################################################################################
#파일 콘테츠 읽기, 상대 경로와 절대 경로, 행 단위로 접근하기

# 현재 작업 디렉토리 출력
print("현재 작업 디렉토리:", os.getcwd())

# 이동할 디렉토리 경로를 설정합니다.
new_path = "partial_programs/reading_from_a_file"  # 변경할 경로로 수정
# 디렉토리를 변경합니다.
os.chdir(new_path)
# 변경된 작업 디렉토리 출력
print("변경된 작업 디렉토리:", os.getcwd())

path = Path('pi_digits.txt')
path.read_text()      # 읽어서 찍어냄
contents = path.read_text()
contents = contents.rstrip().lstrip()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    line = line.lstrip()
    pi_string += line
    print(f"각 줄은 = {line}")

print(pi_string)
print(len(pi_string))


###################################################################################
#백만 단위의 큰 콘텐츠 다루기

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
print(f"줄 수={len(lines)}")
for line in lines[:5]:
    # print(f"각 줄={line}")
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

####################################################################################
#원주율 속에 생일이 있을까?

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")