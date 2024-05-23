# 최댓값
"""
문제
<그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성하시오.

예를 들어, 다음과 같이 81개의 수가 주어지면

 	1열	2열	3열	4열	5열	6열	7열	8열	9열
1행	3	23	85	34	17	74	25	52	65
2행	10	7	39	42	88	52	14	72	63
3행	87	42	18	78	53	45	18	84	53
4행	34	28	64	85	12	16	75	36	55
5행	21	77	45	35	28	75	90	76	1
6행	25	87	65	15	28	11	37	28	74
7행	65	27	75	41	7	89	78	64	39
8행	47	47	70	45	23	65	3	41	44
9행	87	13	82	38	31	12	29	29	80
이들 중 최댓값은 90이고, 이 값은 5행 7열에 위치한다.

입력
첫째 줄부터 아홉 번째 줄까지 한 줄에 아홉 개씩 수가 주어진다. 주어지는 수는 100보다 작은 자연수 또는 0이다.

출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 위치한 행 번호와 열 번호를 빈칸을 사이에 두고 차례로 출력한다. 최댓값이 두 개 이상인 경우 그 중 한 곳의 위치를 출력한다.

예제 입력 1 
3 23 85 34 17 74 25 52 65
10 7 39 42 88 52 14 72 63
87 42 18 78 53 45 18 84 53
34 28 64 85 12 16 75 36 55
21 77 45 35 28 75 90 76 1
25 87 65 15 28 11 37 28 74
65 27 75 41 7 89 78 64 39
47 47 70 45 23 65 3 41 44
87 13 82 38 31 12 29 29 80

예제 출력 1 
90
5 7
"""
### 이중 리스트###


## matrix 객체를 enumerate로 열(index)값과 행(value)값을 뽑아, 튜플형태로 리스트에 저장, 리스트 object로 변환하여 결과값 출력
matrix = []
lst_max = []

# 9행까지 각 줄을 입력받아 리스트로 변환하여 추가
for _ in range(9):
    row = list(map(int, input().split()))
    matrix.append(row)

# 각 행의 최댓값을 row_max 객체('int' object) 저장 => 리스트(lst_max)에 저장하여 'list' object로 변환
for idx, row in enumerate(matrix):
    row_max = max(row)
    # row 리스트에서 row_max값이 처음으로 나타나는 인덱스, 최댓값이 있는 열의 인덱스를 저장
    idx_max = row.index(row_max)
     # 최댓값, 최댓값 인덱스, 행 인덱스를 튜플로 저장
    lst_max.append((row_max, idx, idx_max))

# 최댓값 중에서 가장 큰 값과 해당 행, 열 인덱스 출력, 인덱스를 1부터 시작하도록 수정
max_value, max_row, max_col = max(lst_max)
print(f"{max_value}\n{max_row + 1} {max_col + 1}")


## 리스트 컴프리헨션
matrix = [list(map(int, input().split())) 
          for _ in range(9)]
lst_max = [(max(row), idx, row.index(max(row))) 
           for idx, row in enumerate(matrix)]

max_value, max_row, max_col = max(lst_max)
print(f"{max_value}\n{max_row + 1} {max_col + 1}")


## 일반적인 경우, 이중 for문
matrix = [list(map(int, input().split())) 
         for _ in range(9)]

max_num, max_row, max_col = 0, 0, 0

for row in range(9):
    for col in range(9):
        if max_num <= matrix[row][col]:
            max_row = row + 1
            max_col = col + 1
            max_num = matrix[row][col]

print(f"{max_num}\n{max_row} {max_col}")


## 일반적인 경우, 리스트 컴프리헨션 + 튜플 사용
matrix = [list(map(int, input().split())) 
          for _ in range(9)]

max_num, max_row, max_col = max (
    (matrix[row][col], row + 1, col + 1) 
    for row in range(9) for col in range(9)
)

print(f"{max_num}\n{max_row} {max_col}")


## 일반적인 경우, 더 직관적 변환
matrix = [[int(x) for x in input().split()] 
          for _ in range(9)]

max_num, max_row, max_col = max (
    (matrix[row][col], row + 1, col + 1) 
    for row in range(9) for col in range(9)
)

print(f"{max_num}\n{max_row} {max_col}")