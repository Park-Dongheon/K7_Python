message = input("입력값: ")    # prompt - cursor, input()으로 받는 숫자는 string 타입
message = int(message)         # 문자열을 숫자로 변환 - Java: Integer.parseInt();
sum = message + 20
print(sum, message)

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:                                            # 빈 리스트이면 False, 아닐경우 True
    current_user = unconfirmed_users.pop()                          # 리스트의 마지막 요소부터 하나씩 꺼냄
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')                                              # 리스트의 요소를 제거
print(pets)