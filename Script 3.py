import pandas as pd
import math


data_1 = {
        'Car_Manufacturer': ['Toyota', 'Hyundai', 'Honda', 'Ford', 'Volkswagen', 'Nissan', 'Kia', 'Mazda'],
        'Mileage': [25, 12.5, 23.1, 12, 17, 13, 15, float('nan')],
        'Satisfaction': ['Higher', 'Lower', 'Higher', 'Medium', 'Medium', 'Lower', 'Medium', 'Lower'],
    }

mileages_notMissing = []
for mileage in data_1['Mileage']:
    if not math.isnan(mileage):
        mileages_notMissing.append(mileage)

meanMileage = sum(mileages_notMissing) / len(mileages_notMissing)

imputedMileages = []
for mileage in data_1['Mileage']:
    if math.isnan(mileage):
        imputedMileages.append(meanMileage)
    else:
        imputedMileages.append(mileage)

data_1['Mileage'] = imputedMileages

print("Imputed data:")
numberOfCars = len(data_1['Car_Manufacturer'])
for i in range(numberOfCars):
    car = data_1['Car_Manufacturer'][i]
    mileage = data_1['Mileage'][i]
    print(f"{car}: {mileage:.1f}")