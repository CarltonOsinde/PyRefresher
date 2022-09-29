user_input = ''
all_the_responses = []

while True:
    user_input = input("Say something: ")
    all_the_responses.append(user_input)
    if user_input == 'Stop':
        break
    else:
        continue

print(all_the_responses)
