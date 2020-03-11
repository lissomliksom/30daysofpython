# File used for importing into 8.15.py

def print_models(unprintet_designs, completed_models):
  '''
  Simulate printing each design, until none are left.
  Move each design to completed models after printing.
  '''
  while unprintet_designs:
    current_design = unprintet_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
  ''' Show all the models that were printed '''
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)