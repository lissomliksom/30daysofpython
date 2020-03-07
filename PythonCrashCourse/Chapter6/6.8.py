# Store dictionaries in a list. Loop through the list and print content of dictionaries.
pets = [
  {'Animal': 'Cat', 'Owner': 'Simen'},
  {'Animal': 'Lemur', 'Owner': 'Erlend'},
  {'Animal': 'Goldfish', 'Owner': 'Tormod'},
  {'Animal': 'Rhinoceros', 'Owner': 'John Doe'}
]

for pet in pets:
  print(f"{pet['Owner']} owns a {pet['Animal'].lower()}")