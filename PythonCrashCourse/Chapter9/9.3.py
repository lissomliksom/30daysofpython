class User():
  ''' Receive and output info about a user to our website '''

  def __init__(self, first_name, last_name, username, location):
    ''' Store basic information about user '''
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.location = location
  
  def describe_user(self):
    ''' Print a summary of the users information '''
    name = f"{self.first_name.title()} {self.last_name.title()}"
    summary = f"'{self.username}', real name {name}, is located in {self.location}"
    print(summary)

  def greet_user(self):
    ''' Print a personalized greeting '''
    print(f"Hello {self.username}. Thank you for logging in")


admin = User('Tiberius', 'Starthorn', 'admin', 'Oslo')
moderator = User('Jane', 'Doe', 'mod', 'Bergen')
user_1 = User('John', 'Doe', 'Enthusiastic_user', 'Trondheim')
user_2 = User('Edgar', 'Allan Poe', 'Poe(t)', 'Stavanger')

admin.describe_user()
admin.greet_user()

moderator.describe_user()
moderator.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()