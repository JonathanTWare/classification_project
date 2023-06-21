import pandas as pd
import numpy as np
from env import get_db_url
import os


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

def get_telco_data():
    if os.path.isfile('telco_df.csv'):
        df = pd.read_csv('telco_df.csv', index_col = 0)

    else:

        df = new_telco_data()

        df.to_csv('telco_df.csv')
        return df



