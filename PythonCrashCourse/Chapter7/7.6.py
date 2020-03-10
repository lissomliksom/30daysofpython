# Improve upon 7.5. Allow users to quit, use an active-variable to control how long the loop runs.

prompt = "\nTell me your age and I will tell you the price of your movie ticket."
prompt += "\nType 'quit' to stop."
prompt += "\nMy age is: "
message = "Your movie ticket will cost "

active = True

while active:
  age = input(prompt)
  
  if age == 'quit':
    active = False
  else:
    age = int(age)
    print(age)
    if age < 3:
      print("Your movie ticket is free!")
    elif age >= 3 and age <= 12:
      print(f"{message} $12")
    else:
      print(f"{message} $15")


