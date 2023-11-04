import pandas as pd

def seperate_transactions(read_file_name, write_file_name, filter_condition=None, column_names_list=None):
    # Read the data
    raw_data = pd.read_csv(read_file_name)
    # Clean the data by column, and filter_value 
    if column_names_list is None:
        cleaned_data = raw_data.loc[raw_data[filter_condition[0]] == filter_condition[1], :]
    elif filter_condition is None:
        cleaned_data = raw_data.loc[:, column_names_list]
    else:
        cleaned_data = raw_data.loc[raw_data[filter_condition[0]] == filter_condition[1], column_names_list]
    # Write the data to a new file
    cleaned_data.to_csv(write_file_name)


filter = ['item_type', 'Beverages']
only_columns = ['item_name', 'transaction_amount']

seperate_transactions('fast_food_sales.csv', 'test.csv', filter, only_columns)


