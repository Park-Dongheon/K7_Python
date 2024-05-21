from pathlib import Path
import os

print("현재 작업 디렉토리 : ", os.getcwd())

new_path = 'partial_programs/reading_from_a_file'
os.chdir(new_path)

print("변경후 작업 디렉토리 : ", os.getcwd())

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