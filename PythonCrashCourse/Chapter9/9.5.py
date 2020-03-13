class User():
  ''' Receive and output info about a user to our website '''

  def __init__(self, first_name, last_name, username, location):
    ''' Store basic information about user '''
    self.first_name = first_name
    self.last_name = last_name
    self.username = username
    self.location = location
    self.login_attempts = 0
  
  def describe_user(self):
    ''' Print a summary of the users information '''
    name = f"{self.first_name.title()} {self.last_name.title()}"
    summary = f"'{self.username}', real name {name}, is located in {self.location}"
    print(summary)

  def greet_user(self):
    ''' Print a personalized greeting '''
    print(f"Hello {self.username}. Thank you for logging in")

  def increment_login(self, login_attempts):
    ''' Increment the number of login attempts '''
    self.login_attempts += 1

  def reset_login_attempts(self):
    ''' Reset login attempts to zero '''
    self.login_attempts = 0

user_1 = User('Tiberius', 'Starthorn', 'Mayor345', 'Oslo')

# Increment login attempts and output number of login attempts
print(f"Login attempts: {user_1.login_attempts}")
user_1.increment_login(1)
print(f"Login attempts: {user_1.login_attempts}")
user_1.increment_login(1)
print(f"Login attempts: {user_1.login_attempts}")
user_1.increment_login(1)
print(f"Login attempts: {user_1.login_attempts}")

# Reset login attempts
user_1.reset_login_attempts()
print(f"Login attempts successfully reset. Current login attempts: {user_1.login_attempts}")