import requests
from bs4 import BeautifulSoup

# header에 넣을 자신의 User-Agent 정보
user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}

# 요청 시, get 메서드 두 번째 인자에 헤더 정보를 넣을 수 있는데, 이 때 User-Agent 값을 넘겨줄 수 있음
res = requests.get("https://qna.programmers.co.kr/", user_agent)

# 응답을 바탕으로 BeautifulSoup 객체를 생성
soup = BeautifulSoup(res.text, "html.parser")

questions = soup.find_all("li", "question-list-item")
for question in questions:
    print(question.find("div", "question").find("div", "top").h4.text)