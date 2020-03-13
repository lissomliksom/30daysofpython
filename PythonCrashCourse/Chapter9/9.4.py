'''
Honestly, I struggled A LOT with this example. 
Will repeat later for more practice.
'''



class Restaurant():
  ''' Store and output information about one or more restaurants '''

  def __init__(self, restaurant_name, cuisine_type):
    ''' Initialize name and type of restaurant '''
    self.name = restaurant_name
    self.cuisine = cuisine_type
    self.number_served = 0

  def describe_restaurant(self):
    ''' Print a description of the restaurant '''
    print(f"{self.name} is a restaurant specializing in {self.cuisine}")

  def open_restaurant(self):
    ''' Print a message stating that the restaurant is open '''
    print(f"{self.name} is open.")

  def set_number_served(self, number_served):
    ''' Sets the number of served customers '''
    self.number_served = number_served

  def increment_number_served(self, additional_served):
    ''' Add new customers to the amount served '''
    self.number_served += additional_served
    

# Create an instance. Remember to only use the same number of positional arguments as in __init__
restaurant = Restaurant('Pasta-bilities', 'pasta')

restaurant.describe_restaurant()

# Call the new method through our instance created above. Outputs default value.
print(f"It has served {restaurant.number_served} customers")

# Set new number of customers served
restaurant.number_served = 43
print(f"By 11:00 it has served {restaurant.number_served} customers")

# Set new number of customers served
restaurant.set_number_served(55)
print(f"By 17:00 it has served {restaurant.number_served} customers")

# Increments number of customers served
restaurant.increment_number_served(45)
print(f"At the end of the day, a total of {restaurant.number_served} were served.")