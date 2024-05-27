from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv
import json

# csv 파일 경로
path = Path('fire_data/modis_2022_Republic_of_Korea.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, colum_header in enumerate(header_row):
    print(index, colum_header)

lats, lons, brightness, dates, time  = [], [], [], [], []        # 파이썬의 간결한 코딩, 리스트 객체 여러개 정의

for row in reader:
    try:
        date = datetime.strptime(row[5], "%Y-%m-%d")
        lat = float(row[0])          # 빈 문자열을 정수로 변경 불가, 데이터 누락 대응 필요
        lon = float(row[1])
        bright = float(row[2])
        t = int(row[6])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        lats.append(lat)
        lons.append(lon)
        brightness.append(bright)
        time.append(t)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, lats, color="red", alpha=0.5)
ax.plot(dates, lons, color="blue", alpha=0.5)
ax.plot(dates, brightness, color="green", alpha=0.5)
ax.fill_between(dates, lats, lons, facecolor='yellow', alpha=0.9)      # alpha: 음영 속성

ax.set_title("Republic of Korea fire, 2022", fontsize=24)
ax.set_xlabel('Time', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Brightness', fontsize=10)
ax.tick_params(labelsize=8)

plt.show()