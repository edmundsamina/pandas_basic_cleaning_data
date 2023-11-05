import pandas as pd

# using pandas .loc to filter data by column and rows => .loc[row, column]

# Reusable function to extract, transform and load data using .loc[]
def seperate_transactions_with_loc(read_file_name, write_file_name, filter_condition=None, column_names_list=None):
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



# Reusable function to extract, transform and load data using .iloc[]
def seperate_transactions_with_iloc(read_file_name, write_file_name, row_index=None, column_index=None):
    raw_data = pd.read_csv(read_file_name)
    # Clean the data by column, and filter_value 
    if row_index is None:
        cleaned_data = raw_data.iloc[:, column_index[0]: column_index[1]]
    elif column_index is None:
        cleaned_data = raw_data.iloc[row_index[0]:row_index[1], :]
    # Write the data to a new file
    cleaned_data.to_csv(write_file_name)


def largest_spends(nth_rows, column_name, file_name):
    raw_data = pd.read_csv(file_name)
    print(raw_data.nlargest(nth_rows, [column_name]))



seperate_transactions_with_iloc('fast_food_sales.csv', 'test2.csv', column_index=[0, 3])
largest_spends(5, 'transaction_amount', 'fast_food_sales.csv' )
