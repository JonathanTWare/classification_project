from sklearn.model_selection import train_test_split
import pandas as pd
from pydataset import data
from env import get_db_url
import acquire
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer




#----------------------------------TELCO----------------------------------------------
def prep_telco_data(df):
    df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'], inplace=True)
      
   # Cleaning and transforming 'total_charges' column
  
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
   
   
        # Encoding categorical variables

    df['total_charges'] = df.total_charges.astype(float)
    df['has_churned'] = df.churn.map({'Yes': 1, 'No': 0})
    df['gender_female'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn'] = df.churn.map({'Yes': 1, 'No': 0})
    

    # Creating dummy variables
    dummy_df = pd.get_dummies(df[['multiple_lines', \
                              'online_security', \
                              'online_backup', \
                              'device_protection', \
                              'tech_support', \
                              'streaming_tv', \
                              'streaming_movies', \
                              'contract_type', \
                              'internet_service_type', \
                              'payment_type']], dummy_na=False, \
                              drop_first=True)
    
    df = pd.concat([df, dummy_df], axis=1)
    
    train, validate, test = split_telco_data(df)
    
    return train, validate, test

    """
    Splits the Telco data into train, validate, and test sets.
    
    Parameters:
    - df: pandas DataFrame
        Input DataFrame containing the Telco data.
    
    Returns:
    - train: pandas DataFrame
        Training dataset.
    - validate: pandas DataFrame
        Validation dataset.
    - test: pandas DataFraxme
        Test dataset.
    """
    

def split_telco_data(df):
  
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.churn)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.churn)
    
   

    return train, validate, test
