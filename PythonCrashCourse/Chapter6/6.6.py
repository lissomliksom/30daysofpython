wanted_respondents = ['jen', 'simen', 'edward', 'erlend', 'tormod']

favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python'
}

# Loop through the list of people that should take the poll.
for person in wanted_respondents:
  if person in favorite_languages.keys():
    print(f"*** Great job {person.title()} ***. Thank you for taking our poll!\n")
  else:
    print(f"Please take our poll, {person.title()}.\n")