def make_shirt(size, text):
  ''' Print info about shirt. '''
  print(f"Your shirt is size {size.title()}")
  print(f"Your chosen message: '{text}'\n")

# Call the function using positional arguments
make_shirt("M", "Hasta la vista, baby")

# Call the function using keyword arguments
make_shirt(size = "s", text = "I'll be back")
make_shirt(text = "Governator", size = "L")