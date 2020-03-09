# Modify and improve upon 6.2.py. Allow more numbers, loop through all values.
favorite_numbers = {
  'Simen': [93, 7, 14, 21],
  'Erlend': [2.71828, 23],
  'Tormod': [3.1415, 666],
  'Andreas': [42, 777],
  'Jarl': [2112]
}

# Print all numbers as array:
for favorite in favorite_numbers:
  print(f"{favorite}", end=": ")
  print(favorite_numbers[favorite])

print("\n***\n")

# Print all numbers individually:
for favorite in favorite_numbers:
  # Print name
  print(f"{favorite}", end=": ")

  # Loop through all numbers in array of numbers
  for number in favorite_numbers[favorite]:

    # Print each individual number
    print(number, end=" ")

  # Print new line to separate names  
  print("\n")