usernames = ['Simen', 'Erlend', 'Tormod', 'Admin', 'Andreas']

for user in usernames:
  if user == 'Admin':
    print("Hello admin. Would you like to see a status report?")
  else:
    print(f"Hello {user}, thank you for logging in")