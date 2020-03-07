# Check if usernames are unique. Make sure comparisons are case sensitive

current_users = ['Simen', 'TacocaT', 'qwerty', 'Tormod', 'Erlend', 'Indigo']
new_users = ['SIMEN', 'Tacocat', 'Jarl', 'Eirik', 'Indigo']

current_users_lowercase = []
for user in current_users:
  current_users_lowercase.append(user.lower())

for new in new_users:
  if new.lower() in current_users_lowercase:
    print(f"Username '{new}' is not available. Please select a new username.")
  else:
    print(f"Username {new} is available.")