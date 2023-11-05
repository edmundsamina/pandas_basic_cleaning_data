import pandas as pd
import os

# Extract, transform and load data to a new file 
raw_data = pd.read_csv('fast_food_sales.csv')
cleaned_data = raw_data.loc[raw_data['time_of_sale'] == 'Morning', :]
cleaned_data.to_csv('morning_sales.csv')

# Checking the file path exists 
file_exists = os.path.exists('morning_sales.csv')
print(file_exists)