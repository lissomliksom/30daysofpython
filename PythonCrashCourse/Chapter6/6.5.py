rivers = {
  'nile': 'egypt',
  'yangtze': 'china',
  'amazon': 'south america'
}

# Use a loop to print a senctence about each river.
for river in rivers.keys():
  print(f"The {river.title()} runs through {rivers[river].title()}.")

print("\n")

# Use a loop to print the name of each river included in the dictionary.
for river in rivers.keys():
  print(f"{river.title()}", end="\t\t")

print("\n")

# Use a loop to print the name of each country included in the dictionary.
for country in rivers.values():
  print(f"{country.title()}", end="\t\t")