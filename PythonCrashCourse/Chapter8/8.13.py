def build_profile(first, last, **user_info):
  ''' Build a dictionary containing everything we know about a user '''
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_profile = build_profile('Tiberius', 'Starthorn', age='48', location='Faerun', occupation='Full-time teddybear')

print(user_profile)