from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

dates, falls = [], []
for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        fall = float(row[3])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        falls.append(fall)
print(falls)

# 강우량 그래프 그리기
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, falls, color='blue')

# 그래프 형식
ax.set_title("Death Valley, 2021", fontsize=20)
ax.set_xlabel('Daily Rainfall', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel('Falls', fontsize=12)
ax.tick_params(labelsize=16)

plt.show()
