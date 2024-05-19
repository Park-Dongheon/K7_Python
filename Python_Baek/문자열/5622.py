# 다이얼
"""
문제
상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.



전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.

숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.

상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.

출력
첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

예제 입력 1 
WA

예제 출력 1 
13

예제 입력 2 
UNUCIC

예제 출력 2 
36
"""

word = list(map(str, input().upper()))
time_sum = 0

for ch in word:
    num = 1
    time = 2
    if(ch == 'A' or ch == 'B' or ch == 'C'):
        num = 2
        time += 1
    elif(ch == 'D' or ch == 'E' or ch == 'F'):
        num = 3
        time += 2
    elif(ch == 'G' or ch == 'H' or ch == 'I'):
        num = 4
        time += 3
    elif(ch == 'J' or ch == 'K' or ch == 'L'):
        num = 5
        time += 4
    elif(ch == 'M' or ch == 'N' or ch == 'O'):
        num = 6
        time += 5
    elif(ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S'):
        num = 7
        time += 6
    elif(ch == 'T' or ch == 'U' or ch == 'V'):
        num = 8
        time += 7
    elif(ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z'):
        num = 9
        time += 8
    else:
        num = 0
        time += 9
    time_sum += time

print(time_sum)

# 일반적인 경우
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
alpha = list(input())		# 알파벳 단어 입력
result = 0

for i in alpha:
    for j in dial:
        if i in str(j):		# str(j) = 'A', 'B', 'C', •••
            num = dial.index(j) + 3		# 각 알파벳 별 필요한 시간
            result += num

print(result)