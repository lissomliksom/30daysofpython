#Make and print a list of the first ten cubes, using a list comprehension
numbers = [value**3 for value in range(1,11)]
for number in numbers:
  print(number)