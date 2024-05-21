import os

base_path = os.getcwd()
folder_prefix = "Guest book"

#폴더 확인 함수
def check_folders(base_path, folder_prefix, start, end):
    for i in range(start, end + 1):
        folder_path = os.path.join(base_path, f"{folder_prefix}{i}")
        if os.path.exists(folder_path):
            print(f"{folder_path} exists.")
        else:
            print(f"{folder_path} does not exist.")

#폴더 생성 코드
os.makedirs(base_path, exist_ok=True)
os.mkdir(os.path.join(base_path, folder_prefix))

#생성된 폴더 확인
check_folders(base_path, folder_prefix, 1, 1)

response = input()
# 파일 생성 및 쓰기


print("File created and written successfully.")