# Adding a conditional check to make sure the list of users is not empty
usernames = ['Simen', 'Erlend', 'Tormod', 'Admin', 'Andreas']

if usernames:
  for user in usernames:
    if user == 'Admin':
      print("Hello admin. Would you like to see a status report?")
    else:
      print(f"Hello {user}, thank you for logging in")
else:
  print("We need to find some users")