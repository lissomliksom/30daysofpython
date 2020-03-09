'''
GOAL:
Create a dictionary of users. 
Format, print and do calculations with info from dictionary. 
''' 

users = {
  'user_001': {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'gender': 'M', 'city': 'Trondheim'},
  'user_002': {'first_name': 'Jane', 'last_name': 'Doe', 'age': 20, 'gender': 'F', 'city': 'Oslo'},
  'user_003': {'first_name': 'phil', 'last_name': 'Anderson', 'age': 60, 'gender': 'M', 'city': 'Bergen'},
  'user_004': {'first_name': 'Marie', 'last_name': 'johansen', 'age': 55, 'gender': 'F', 'city': 'Stavanger'},
}

users_age = 0

print("Our users:")

# Use loop to print ID and information about each user
for user, info in users.items():
  # Print user ID
  print(f"ID {user[-3:]}: ", end="")

  # Print selected user info
  print(f"{info['first_name'].title()} {info['last_name'].title()}, aged {info['age']}")

  # Add total user age
  users_age += info['age']

# Calculate average user age by dividing total age / number of users
print(f"\nAverage user age: {users_age/len(users.keys())}")