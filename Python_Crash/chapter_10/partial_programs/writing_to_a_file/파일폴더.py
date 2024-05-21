with open("example.txt", encoding='utf-8') as file:
  data = file.read()
  print(data)

import os
directory = os.getcwd()
flist = os.listdir(directory)       # 현재 경로에 있는 파일들을 리스트 형태로 보여줌
print(flist)