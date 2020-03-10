sandwich_orders = ['Pastrami', 'Ham', 'Tuna', 'Brie', 'Gouda']
finished_sandwiches = []

while sandwich_orders:
  completed = sandwich_orders.pop()
  print(f"I made your {completed} sandwich.")
  finished_sandwiches.append(completed)

print("\n***")
print("Each sandwich made:")
print(finished_sandwiches)