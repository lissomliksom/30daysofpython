# Writing a simple function with PEP 8 in mind.

def address_book(
    first_name, last_name,
    country, state, city, street, middle_name=''):
  ''' Format and print name and address'''
  name = f"\n{first_name.title()} {middle_name.title()} {last_name.title()}"
  address = f"{street.title()}, {city.title()} {state.title()}, {country.title()}"
  print(name)
  print(address)

address_book('Tiberius', 'Starthorn', 'United States', 'Massachusetts', 'Springfield', '1st Simpson Street')