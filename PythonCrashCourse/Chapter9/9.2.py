class Restaurant():
  ''' Store and output information about one or more restaurants '''

  def __init__(self, restaurant_name, cuisine_type):
    ''' Initialize name and type of restaurant '''
    self.name = restaurant_name
    self.cuisine = cuisine_type

  def describe_restaurant(self):
    ''' Print a description of the restaurant '''
    print(f"'{self.name}' is a restaurant specializing in {self.cuisine}")

  def open_restaurant(self):
    ''' Print a message stating that the restaurant is open '''
    print(f"'{self.name}' is open.")

# Create an instance for three different restaurants
restaurant_1 = Restaurant('Pasta-bilities', 'pasta')
restaurant_2 = Restaurant('Wok this way', 'asian dishes')
restaurant_3 = Restaurant('Lord of the Fries', 'potatoes')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()