from pathlib import Path
import json
from datetime import datetime

import plotly.express as px

# 데이터를 문자열로 읽어 파이썬 객체로 변환
path = Path('fire_data/modis_2022_Republic_of_Korea.json')
contents = path.read_text()
k_fire_datas = json.loads(contents)

# 데이터 집합의 화제 데이터를 모두 읽음
header_row = k_fire_datas[0].keys()
print(len(k_fire_datas))

for index, colum_header in enumerate(header_row):
    print(index, colum_header)

# 위도, 경도, 밝기, 날짜, 시간을 저장할 리스트
lats, lons, bright, dates, times = [], [], [], [], []
for k_fire_data in k_fire_datas:
    try:
        # date = datetime.strptime(k_fire_data["acq_date"], "%Y-%m-%d")
        time = datetime.strptime(k_fire_data["acq_time"], "%H%M")
        lat = k_fire_data["latitude"]
        lon = k_fire_data["longitude"]
        brightness = k_fire_data["brightness"]
    except ValueError:
        print(f"Missing data for")
    else:            
        # dates.append(date.strftime("%Y-%m-%d"))
        times.append(time.strftime("%H:%M"))
        lats.append(lat)
        lons.append(lon)
        bright.append(brightness)

print(lats[:10])
print(lons[:10])
print(bright[:10])

# 지도 그리기
title = "Korea Fire Outbreak"
fig = px.scatter_mapbox(
    lat=lats,
    lon=lons,
    # mode='markers',
    dict(
        size=bright,  # 각 점의 크기를 화재 규모에 따라 설정
        color=bright,  # 각 점의 색상을 화재 규모에 따라 설정
        colorscale='Reds',  # 색상 척도 설정
        opacity=0.7,  # 불투명도
        colorbar=dict(title='Brightness')
    ),
    hovertext=[f'Latitude: {lat}, Longitude: {lon}, Brightness: {b}' for lat, lon, b in zip(lats, lons, bright)]
    # outbreak=bright,
    # hover_name='Date',
    # hover_data={'Time': times},
    # projection='natural earth'
)

fig.show()