def make_car(manufacturer, model, **car_info):
  ''' Store information about car in dictionary '''
  car_info['manufacturer'] = manufacturer.title()
  car_info['model'] = model.title()
  return car_info

car_1 = make_car('Subaru', 'outback', color='blue', tow_package=True)
car_2 = make_car('lamborghini', 'diablo', color='yellow', spare_wheels=2, special_rims=True)

print(car_1)
print(car_2)