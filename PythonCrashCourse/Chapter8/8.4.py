def make_shirt(size = 'L', text = 'I love Python'):
  ''' Print info about shirt. Shirts have default values'''
  print(f"Your shirt is size {size.title()}")
  print(f"Your chosen message: '{text}'\n")

# Use default values
make_shirt()

# Make medium shirt with default message
make_shirt("M")

# Make custom shirt
make_shirt("S", "Python is for girls")
