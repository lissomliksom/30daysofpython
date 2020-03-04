# Copy a list
pizzas = ['pepperoni', 'ham', 'bacon', 'vegetarian']
friend_pizzas = pizzas[:]

# Add different pizzas to the different lists.
pizzas.append('pineapple')
friend_pizzas.append('vegan')

# Use two for-loops to prove that I now have to separate lists
print("\nMy favorite pizzas are:")
for fav in pizzas:
  print("\t", fav)

print("\nMy friend's favorite pizzas are:")
for fav in friend_pizzas:
  print("\t", fav)