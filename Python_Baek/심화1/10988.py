# 팰린드롬인지 확인하기
"""
문제
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.

팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 

level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

입력
첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

출력
첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.

예제 입력 1 
level

예제 출력 1 
1

예제 입력 2 
baekjoon

예제 출력 2 
0
"""

pel = input()
string_l1 = []
string_l2 = []
for ch in pel:
    string_l1.append(ch)
for ch in reversed(pel):
    string_l2.append(ch)
if(string_l1 == string_l2):
    is_pel = 1
else:
    is_pel = 0

print(is_pel)


# 파이썬 style
word = list(str(input()))

if list(reversed(word)) == word:
    print(1)
else:
    print(0)


# 리스트 슬라이싱 사용
word = list(input())

if word == word[::-1]:
    print(1)
else :
    print(0)


# 리스트 컴프리헨션
word = input()
print(1 if word == word[::-1] else 0)