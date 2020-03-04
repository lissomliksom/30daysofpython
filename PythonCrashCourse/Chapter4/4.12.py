# Copy, append, then loop through all foods in list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy foods:")
for food in my_foods:
  print(food)

print("\nMy friend's foods:")
for food in friend_foods:
  print(food)