"""
문제
시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
시험 성적을 출력한다.

예제 입력 1 
100

예제 출력 1 
A
"""

# if-elif-else 조건문
score = int(input())
if (90 <= score and score <= 100):
    print('A')
elif (80 <= score and score <= 89):
    print('B')
elif (70 <= score and score <= 79):
    print('C')
elif (60 <= score and score <= 69):
    print('D')
else:
    print('F')

score = int(input())
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

# 삼항 연산자
score = int(input())
print('A') if score >= 90 else print('B') if score >= 80 else print('C') if score >= 70 else print('D') if score >= 60 else print('F')