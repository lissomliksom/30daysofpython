def city_country(city, country):
  ''' Return values from a function '''
  fact = f"{city}, {country}"
  return fact.title()

print(city_country("Santiago", "Chile"))
print(city_country("Cancun", "mexico"))
print(city_country("toronto", "Canada"))