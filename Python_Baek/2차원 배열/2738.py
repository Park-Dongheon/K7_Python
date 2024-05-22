# 행렬 덧셈
"""
문제
N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

입력
첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

출력
첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

예제 입력 1 
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100

예제 출력 1 
4 4 4
6 6 6
5 6 100
"""

# First_Coding - 실행시간이 높아 통과x, Runtime err
# n, m = map(int, input().split())

# matrix_a = []
# for _ in range(n):
#     row = list(map(int, input().split()))
#     matrix_a.append(row)

# matrix_b = []
# for _ in range(m):
#     row = list(map(int, input().split()))
#     matrix_b.append(row)

# matrix = []
# for i in range(n):
#     row = []
#     for j in range(m):
#         row.append(matrix_a[i][j] + matrix_b[i][j])
#     matrix.append(row)

# for row in matrix:
#     # * 연산자는 리스트 언패킹(unpacking)을 수행, 이를 사용하면 리스트의 각 요소를 개별적인 인자로 전달, 리스트의 요소를 반복문 없이 간편하게 출력할 수 있는 방법
#     print(*row)


# 리스트 컴프리헨션 사용
n, m = map(int, input().split())

# 행렬 A 입력
matrix_a = [list(map(int, input().split())) for _ in range(n)]

# 행렬 B 입력
matrix_b = [list(map(int, input().split())) for _ in range(n)]

# 행렬의 합 계산, 리스트 컴프리헨션 사용
matrix = [[matrix_a[i][j] + matrix_b[i][j] for j in range(m)] for i in range(n)]

# 결과 출력
for row in matrix:
    print(*row)


# 일반적인 방법
A, B = [], []

N, M = map(int, input().split())

for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for j in range(N):
    row = list(map(int, input().split()))
    B.append(row)
    
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ')
    print()