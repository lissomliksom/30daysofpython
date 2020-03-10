prompt = "Tell me your age and I will tell you the price of your movie ticket: "
message = "Your movie ticket will cost "

while True:
  age = input(prompt)
  age = int(age)
  
  if age < 3:
    print("Your movie ticket is free!")
  elif age >= 3 and age <= 12:
    print(f"{message} $12")
  else:
    print(f"{message} $15")


