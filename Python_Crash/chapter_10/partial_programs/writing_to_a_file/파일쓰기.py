# 파일 생성 및 쓰기
import os
from pathlib import Path
print(f"현재경로={os.getcwd()}")

with open('example.txt', 'w') as file:            # 파일이 없으면 example.txt 파일 생성, file 변수는 open된 파일 객체
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
    #file.write_text()   --메소드가 없다

print("File created and written successfully.")

# 파일에 내용 추가하기 (append)
path = Path('example.txt')
with path.open(mode='a', encoding='utf-8') as file:
    file.write("path 객체를 사용한 추가 쓰기\n")

# 파일에 내용 추가하기
with open('example.txt', 'a') as file:              # mode: 'a'(append)
    file.write("Adding a new line.\n")
    file.write("Appending another line.\n")

print("Content appended to the file successfully.")

# 새로운 파일 생성하기
try:
    with open('new_file.txt', 'x') as file:
        file.write("This is a newly created file.\n")
    print("New file created and written successfully.")
except FileExistsError:
    print("File already exists.")