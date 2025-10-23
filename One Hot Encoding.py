import pandas as pd

data = {
        'Car_Manufacturer': ['Toyota', 'Hyundai', 'Honda', 'Ford', 'Volkswagen', 'Nissan', 'Kia', 'Mazda'],
        'Mileage': [25, 12.5, 23.1, 12, 17, 13, 15, 9],
        'Satisfaction': ['Higher', 'Lower', 'Higher', 'Medium', 'Medium', 'Lower', 'Medium', 'Lower'],
    }

manufacturers = data['Car_Manufacturer']
#print(manufacturers)
one_hot_encoded_data = []
for currentCar in data['Car_Manufacturer']:
    encoded = {}
    for brand in manufacturers:
        encoded[brand] = 0
    encoded[currentCar] = 1
    one_hot_encoded_data.append(encoded)

for i in range(len(one_hot_encoded_data)):
    Name = data['Car_Manufacturer'][i]
    encoded_data = one_hot_encoded_data[i]
    print(Name + ": " + str(encoded_data))
