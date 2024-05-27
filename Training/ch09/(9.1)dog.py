# 9.1 클래스를 만들고 사용하기

class Dog:      # Dog 클래스 정의
    """개를 표현하는 클래스"""

    def __init__(self, name, age):      # Dog클래스를 기반 인스턴스를 만들 때마다 파이썬이 자동으로 실행, 특별 메서드
        """name과 age 속성 초기화"""
        self.name = name        # 속성 : 인스턴스를 통해 접슨할 수 있는 변수
        self.age = age
    
    def sit(self):
        """앉기"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """구르기"""
        print(f"{self.name} rolled over!")