from pathlib import Path
import json
import os
import plotly.express as px
import requests
# px.colors.named_colorscales()           # 파이썬 터미널에서 색깔 스케일을 확인
# print(os.getcwd())


# Read data as a string and convert to a Python object.
# path = Path('mapping_global_datasets/eq_data/eq_data_30_day_m1.geojson')
# contents = path.read_text(encoding='utf-8')     # 데이터 파일을 문자열로 읽음
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
response = requests.get(url)
contents = response.text
all_eq_data = json.loads(contents)      # 문자열을 json 객체로
# print(all_eq_data)

# Create a more readable version of the data file.
# path = Path('mapping_global_datasets/eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

# 데이터 집합의 지진 데이터를 모두 읽습니다
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))            # 160개

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']      # JSON 데이터의 포멧 형태로 데이터를 가져옴
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

print(f"msg = {mags[:5]}")              # 현재 규모
print(f"longitude = {lons[:5]}")        # 경도
print(f"latitude = {lats[:5]}")         # 위도

title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                    color=mags, color_continuous_scale='Viridis',
                    labels={'color':'Magnitude'},
                    projection='natural earth',
                    hover_name=eq_titles,)
fig.show()