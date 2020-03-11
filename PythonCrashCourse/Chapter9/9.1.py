class Restaurant():
  ''' Store and output information about one or more restaurants '''

  def __init__(self, restaurant_name, cuisine_type):
    ''' Initialize name and type of restaurant '''
    self.name = restaurant_name
    self.cuisine = cuisine_type

  def describe_restaurant(self):
    ''' Print a description of the restaurant '''
    print(f"{self.name} is a restaurant specializing in {self.cuisine}")

  def open_restaurant(self):
    ''' Print a message stating that the restaurant is open '''
    print(f"{self.name} is open.")

# Create an instance
restaurant = Restaurant('Pasta-bilities', 'pasta')

# Print attributes individually
print(f"The restaurant is called '{restaurant.name}'")
print(f"The restaurant serves {restaurant.cuisine}")

# Call methods from class
restaurant.describe_restaurant()
restaurant.open_restaurant()