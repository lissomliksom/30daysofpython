# Modify and improve 6.1. Use dictionaries within a dictionary to store and output information.

people = {
  'person_1': {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'Trondheim'},
  'person_2': {'first_name': 'Jane', 'last_name': 'Doe', 'age': 20, 'city': 'Oslo'},
  'person_3': {'first_name': 'Anon', 'last_name': 'Anonymous', 'age': 45, 'city': 'Bergen'}
}

# Loop through dictionary. Assign one number for key (person), one for item(info).
for person, info in people.items():
  # Print key
  print(f"{person}:", end="\t")

  # Store items in variables and print
  name = f"{info['first_name']} {info['last_name']},"
  additional_info = f"aged {info['age']}, is located in {info['city']}"
  print(name, additional_info)