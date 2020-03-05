# True and False equality and inequality with strings
name = 'Simen'
print(name == 'Simen')
print(name != 'Simen')

# Tests using the lower()-method
name = name.lower()
print(name == 'simen')
print(name == 'Simen')

# Numerical test involving equality and inequality
age = 31
print(age == 31)
print(age != 31)

# Numerical test involving greater than and less than
print(age > 18)
print(age < 30)

# Numerical test involving greater than or equal to
print(age >= 30)
print(age >= 40)

# Numerical test involving less than or equal to
print(age <= 40)
print(age <= 30)

# Tests using the 'and' keyword and the 'or' keyword
print(age >= 30 and name.title() == 'Simen')
print(age < 30 or name == 'Simen')

# Test whether an item is in a list
fruit = ['Banana', 'Apple', 'Pineapple']
print('Apple' in fruit)
print('Pear' in fruit)

# Test wethern an item is not in a list
print('Strawberries' not in fruit)
print('Apple' not in fruit)