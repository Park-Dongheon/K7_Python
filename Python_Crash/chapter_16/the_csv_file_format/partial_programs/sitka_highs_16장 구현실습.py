from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv
import os

path = Path('the_csv_file_format/weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, colum_header in enumerate(header_row):
    print(index, colum_header)

dates, highs, lows = [], [], []        # 파이썬의 간결한 코딩, 리스트 객체 여러개 정의
# for index, colum_header in enumerate(header_row):   # colum_header 첫 번째 행
#     print(index, colum_header)

for row in reader:
    try:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])          # 빈 문자열을 정수로 변경 불가, 데이터 누락 대응 필요
        low = int(row[5])
        # avg = int(row[3])       # 결측치가 있어서 오류 - 중단
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
        # avgs.append(avg)

print(highs)
# print(avgs)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
# ax.plot(dates, avgs, color="green", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.9)      # alpha: 음영 속성

ax.set_title("High and Low Temperature, 2021", fontsize=24)
ax.set_xlabel('Time', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel('Temperature', fontsize=10)
ax.tick_params(labelsize=8)

plt.show()