from pathlib import Path
import json

username = input('이름?')
path = Path('username.json')
contents = path.dumps(username)
path.write_text(contents)
username = json.loads(contents)

print(f"Welcome back, {username}!")