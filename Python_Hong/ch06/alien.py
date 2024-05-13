# {} <-- Set을 표현, 값의 중복이 없음
# 'color, points' <-- Key를 표현, 값을 찾음, Key의 중복이 없음
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])                          # Key 값('color')을 사용하여 찾는 것
print(alien_0['points'])

alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']                   # 키 값을 찾기 > 값을 리턴
print(f"You just earned {new_points} points!")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0                        # 딕셔너리 alien_0에 {키:값}을 추가
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}                                     # 빈 딕셔너리에 {키:값} 추가
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color': 'green'}                     # 딕셔너리의 키에대한 값 수정
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

alien_0 = {'color': 'green', 'points': 5}         # 딕셔너리의 제거, 키 사용
print(alien_0)
del alien_0['points']
print(alien_0)

alien_0 = {'color': 'green', 'speed': 'slow'}     
# print(alien_0['points'])                        # 키 값으로 딕셔너리내의 값 찾기
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.') # 딕셔너리에서 get()으로 key를 찾아 값 찾기, 없으면 None 값을 반환, 오류나지 않음
print(point_value)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]              # aliens 리스트의 원소가 각각 alien_0, alien_1, alien_2의 딕셔너리 형태
for alien in aliens:                              # aliens 리스트의 원소 딕셔너리를 하나씩 출력
  print(alien)

  # Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):                    # loop를 30번 반복, 30마리의 aliens를 만들어 추가
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} # alien을 딕셔너리로 정의하여 빈리스트에 추가
    aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:5]:                          # alien 5마리의 딕셔너리 출력
    print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")