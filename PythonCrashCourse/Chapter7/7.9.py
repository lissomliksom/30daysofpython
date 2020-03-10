sandwich_orders = ['Pastrami', 'Ham', 'Tuna', 'Pastrami', 'Ham', 'Tuna', 'Brie', 'Gouda', 'Brie', 'Pastrami', 'Ham']
finished_sandwiches = []

# Remove all occurrences of 'Pastrami' from sandwich orders.
while 'Pastrami' in sandwich_orders:
  print("We're sorry, we're out of pastrami. Removing order...")
  sandwich_orders.remove('Pastrami')

print(sandwich_orders)
print("\n***")

# Make all remaining sandwiches
while sandwich_orders:
  completed = sandwich_orders.pop()
  print(f"I made your {completed} sandwich.")
  finished_sandwiches.append(completed)

print("\n***")
print("Each sandwich made:")
print(finished_sandwiches)