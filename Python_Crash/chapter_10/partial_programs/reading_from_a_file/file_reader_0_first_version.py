from pathlib import Path
import os

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