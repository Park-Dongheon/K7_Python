from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('the_csv_file_format/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

# lines변수는 리스트
reader = csv.reader(lines)  # reader도 리스트로 간주 : 차이 -- next
## reader는 객체다 - 리스트를 갖고 있다 + 커서 개념을 갖고 있다
header_row = next(reader)

# Extract dates and high temperatures.
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot.
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
