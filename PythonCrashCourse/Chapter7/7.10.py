question = "\nWhat's your dream vacation-destination?"
question += "\n(type 'quit' to end poll)\n"

store_answers = []
active = True

# Store all answers in list.
while active:
  answer = input(question)
  if answer == 'quit':
    active = False
  else:
    store_answers.append(answer)

# Print results
print("\n*** Results ***")
print(store_answers)