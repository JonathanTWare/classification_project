#import libraries
import pandas as pd
import numpy as np
from env import get_db_url
import os

"""
    Retrieves Telco data from a database and returns it as a pandas DataFrame.
    
    Returns:
    - df: pandas DataFrame
        DataFrame containing the Telco data retrieved from the database.
    """
def new_telco_data():
   
    conn = get_db_url('telco_churn')

    query = '''
            SELECT c.*, ct.contract_type, it.internet_service_type, pt.payment_type
            FROM customers AS c
            JOIN contract_types AS ct ON c.contract_type_id = ct.contract_type_id
            JOIN internet_service_types AS it ON c.internet_service_type_id = it.internet_service_type_id
            JOIN payment_types AS pt ON c.payment_type_id = pt.payment_type_id
            '''

    
    df = pd.read_sql(query, conn)
    return df
    """
    Retrieves Telco data either from a CSV file or by calling the new_telco_data function.
    If the data exists in a CSV file, it is loaded from the file. Otherwise, it is retrieved
    from the database and saved to the CSV file for future use.
    
    Returns:
    - df: pandas DataFrame
        DataFrame containing the Telco data.
    """
def get_telco_data():
    if os.path.isfile('telco_df.csv'):
        df = pd.read_csv('telco_df.csv', index_col = 0)

    else:

        df = new_telco_data()

        df.to_csv('telco_df.csv')
        return df



