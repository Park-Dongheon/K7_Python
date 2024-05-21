from pathlib import Path
import json


numbers = [2, 3, 5, 7, 11, 13]

path = Path('numbers.json')         # path에 json데이터로 저장
contents = json.dumps(numbers)
path.write_text(contents)