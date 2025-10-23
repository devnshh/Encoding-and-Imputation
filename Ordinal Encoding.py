import pandas as pd
import math

data = {
        'Car_Manufacturer': ['Toyota', 'Hyundai', 'Honda', 'Ford', 'Volkswagen', 'Nissan', 'Kia', 'Mazda'],
        'Mileage': [25, 12.5, 23.1, 12, 17, 13, 15, 9],
        'Satisfaction': ['Higher', 'Lower', 'Higher', 'Medium', 'Medium', 'Lower', 'Medium', 'Lower'],
    }

dataframe = pd.DataFrame(data)

order = ['Lower', 'Medium', 'Higher']
custom_order = {}
print("Enter a number for each category")
for category in order:
    while True:
        try:
            value = eval(input(f"Enter a number for '{category}': "))
            custom_order[category] = value
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
# print(custom_order)
def OrdinalEncode(dataframe, column, custom_order):
    dataframe_copy = dataframe.copy()
    dataframe_copy[column + "_Encoded"] = dataframe_copy[column].map(custom_order)
    return dataframe_copy

satisfaction_encoded = OrdinalEncode(dataframe, 'Satisfaction', custom_order)
print(satisfaction_encoded)