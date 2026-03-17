'''
Rayaan Hassan
CMSC 111
Spring 2026
Week 7 Assignment 3
'''
car= {
    'brand': 'Toyota',
    'model': 'Camry',
    'year': 2020,
}
#Update the car's year value to 2022
car['year'] = 2022

# Remove the model key-value pair from the dictionary
del car['model']


# Print the updated dictionary
print(car)