# Print info about dictionaries within a dictionary.

cities = {
  'oslo': {
    'country': 'Norway', 
    'population': 693000, 
    'fact': 'Norway\'s largest city'
  },
  'bergen': {
    'country': 'Norway', 
    'population': 257000, 
    'fact': 'Known for its many rainy days'
  },
  'trondheim': {
    'country': 'Norway', 
    'population': 183000, 
    'fact': 'Home to Norway\'s best student society'
  }
}

for city, information in cities.items():
  print(city.title())
  short_info = f"\tCountry: {information['country']}\t\t Population:{information['population']}\n\t{information['fact']}\n"
  print(short_info)