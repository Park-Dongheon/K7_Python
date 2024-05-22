# 단어 공부
"""
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

예제 입력 1 
Mississipi

예제 출력 1 
?

예제 입력 2 
zZa

예제 출력 2 
Z

예제 입력 3 
z

예제 출력 3 
Z

예제 입력 4 
baaa

예제 출력 4
A
"""

# First_Coding - 실행시간이 높아 통과x
# word = input().lower()
# clist = []

# for ch in word:
#     if word.count(ch) > 1 and ch not in clist:
#         clist.append(ch)

# if 2 <= len(clist):
#     print('?')
# else: 
#     print(clist.pop().upper())


## 딕셔너리 이용
# 문자열을 입력받아 대문자 형태로 word 객체 리스트에 저장
word = input().upper()

# 각 알파벳의 등장 횟수를 저장할 딕셔너리를 생성
char_count = {}
for ch in word:
    if ch.isalpha():    # 문자가 알파벳인 경우에만 처리
        char_count[ch] = char_count.get(ch, 0) + 1
        # 딕셔너리인 char_count에서 특정 키 ch의 값을 가져와서 1을 더해 다시 해당 키(char_count[ch])에 대입
        # char_count.get(ch, 0)은 딕셔너리 char_count에서 키 ch에 해당하는 값을 가져옴, 해당 키가 존재하지 않는다면 지정된 기본값인 0을 반환
        
# 등장 횟수가 가장 많은 알파벳 찾기, char_count 딕셔너리에서 가장 큰 값을 가진 알파벳의 등장 횟수가 저장
max_count = max(char_count.values())

# 가장 많은 알파벳을 가진 문자들을 저장
max_chars = [ch for ch, count in char_count.items() if count == max_count]

# 가장 많은 알파벳이 여러 개라면 '?'를 출력, 그렇지 않으면 대문자로 출력
if len(max_chars) >= 2:
    print('?')
else:
    print(max_chars[0])


# 일반적인 방법, set사용 
word = input().upper()
# set함수를 통해 문자열 내 중복문자를 제거하고, 리스트로 변환
word_list = list(set(word))
# 빈 리스트를 생성
lst = []

# 중복문자를 제거한 리스트(word_list)를 반복문을 돌며, count()함수를 통해 입력받은 문자열 내 알파벳 개수를 빈 리스트에 입력
for i in word_list:
    count = word.count(i)
    lst.append(count)

# 가장 많이 사용된 알파벳 개수가 2개 이상일 경우
if lst.count(max(lst))>= 2:
    print("?")
# 가장 많이 사용된 알파벳 개수가 2개 이상이 아닌 경우    
else:
    # 가장 높은 숫자의 인덱스를 통해 중복을 제거한 문자열의 리스트에서 해당 문자를 출력
    print(word_list[lst.index(max(lst))])