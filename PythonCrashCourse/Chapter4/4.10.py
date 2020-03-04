# Make a list of the first ten cubes, using a list comprehension
numbers = [value**3 for value in range(1,11)]

# Use slice to find the first three values in list
print("The first three items in the list are:", numbers[:3])

# Use slice to print three items from the middle of the list
print("Three items from the middle of the list are:", numbers[3:6])

# Use slice to print the last three items from the list
print("The last three items in the list are:", numbers[-3:])