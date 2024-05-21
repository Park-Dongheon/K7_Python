from pathlib import Path
import json

def check_path(path):
    if path.exists():
        contents = path.read_text()
        if path.exists:
            contents = path.read_text()
            username = json.loads(contents)
            print(f"읽기={username}")
        else:
            username = input('이름은?')
            contents = json.dumps(username)
            path.write_text(contents)
            print(f"이름 입력됨={username}")

path = Path('username.json')