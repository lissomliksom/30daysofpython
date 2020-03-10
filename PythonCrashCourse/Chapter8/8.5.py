def describe_city(name, country = 'Norway'):
  ''' Print sentence about city '''
  print(f"{name} is in {country}")

describe_city("Oslo")
describe_city("Reykjavik", "Iceland")
describe_city("Bergen")