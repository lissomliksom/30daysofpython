prompt = "\nPlease enter your desired pizza toppings:"
prompt += "\n(Enter 'quit' to exit)\n"

run = True

while run:
  topping = input(prompt)
  if topping == 'quit':
    run = False
  else:
    print(f"OK, we will add {topping} to your pizza")
