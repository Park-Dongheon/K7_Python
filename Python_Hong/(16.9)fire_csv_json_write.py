import csv
import json
from pathlib import Path

# CSV 파일 경로
csv_file_path = Path('fire_data/modis_2022_Republic_of_Korea.csv')
# JSON 파일 경로
json_file_path = Path('fire_data/modis_2022_Republic_of_Korea.json')

# CSV 파일 읽기
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    data = list(csv_reader)

# JSON 파일 쓰기, indent(들여쓰기)
with open(json_file_path, mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)

print(f"CSV 파일이 {json_file_path}에 JSON 형식으로 저장되었습니다.")