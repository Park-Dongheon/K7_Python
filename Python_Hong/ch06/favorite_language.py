favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()            # 딕셔너리의 키를 이용를 찾는 title() 함수
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():         # 딕셔너리에서 {키:값} 쌍을 받은 items() 함수를 title() 함수를 통해 딕셔너리 출력
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():                    # 딕셔너리에서 key만 받는 keys() 함수
    print(name.title())

for name in favorite_languages.values():                  # 딕셔너리에서 값만 받는 values() 함수
    print(name.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):         # set은 중복을 제거하는데 사용
    print(language.title())

favorite_languages = {                                    # 딕셔너리 원소에 하나의 키에대한 리스트원소값[] 여러개를 가짐
      'jen': ['python', 'rust'],
      'sarah': ['c'],
      'edward': ['rust', 'go'],
      'phil': ['python', 'haskell'],
      }
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:                            # 딕셔너리의 값인 리스트원소값들을 반복하여 출력
        print(f"\t{language.title()}")