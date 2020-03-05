# Write ten conditional tests
# Have five tests evaluate to True and the other five to False


# Easy conditional tests
car = 'Subaru'
print("Is car == 'Subaru'? I predict True.")
print(car == 'Subaru')

print("Is car == 'subaru'? I predict False")
print(car == 'subaru')

car = 'volvo'
print("Is car == 'Volvo'? I predict False.")
print(car == 'Volvo')

car = car.title()
print("Is car == 'Volvo'? I predict True.")
print(car == 'Volvo')


# Tests with if / else, equality and inequality
password = 'Crocodile'
condition_equal = (password.lower() == 'crocodile')
condition_inequal = (password != 'crocodile')

if condition_equal:
  print("\nWelcome to the admin area")

if condition_inequal:
  print("\nAccess denied. Please log in")

number = 12
if number > 20:
  print("\nNumber is more than 20")
else:
  print("\nNumber is less than 20")

# Checking multiple conditions
age = 24
if age == 24 and age/2 == number:
  print("\nage is number * 2")

print(number == 12 and age >= 40)
print(number < 20 and car == 'volvo')