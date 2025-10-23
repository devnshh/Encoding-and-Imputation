import pandas as pd
import math


data_1 = {
        'Car_Manufacturer': ['Toyota', 'Hyundai', 'Honda', 'Ford', 'Volkswagen', 'Nissan', 'Kia', 'Mazda'],
        'Mileage': [25, 12.5, 23.1, 12, 17, 13, 15, float('nan')],
        'Satisfaction': ['Higher', 'Lower', 'Higher', 'Medium', 'Medium', 'Lower', 'Medium', 'Lower'],
    }

dataframe = pd.DataFrame(data_1)
meanMileage = dataframe['Mileage'].mean()
dataframe['Mileage'] = dataframe['Mileage'].fillna(meanMileage)

print("Imputed data:")
print(dataframe)
