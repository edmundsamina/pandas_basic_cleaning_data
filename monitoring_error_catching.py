import pandas as pd
import logging
import os

# Need this to actually get info logged to console, explore why
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
# Extract and transform the data 
def transform(file_path):
    raw_data = pd.read_csv(file_path)
    return raw_data.loc[raw_data['bubbj'], :]
    
try:
    transform('fast_food_sales.csv')
    logging.info('in try block')
except Exception:
    logging.info("invalid key ")
        
