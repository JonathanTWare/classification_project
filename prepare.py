from sklearn.model_selection import train_test_split
import pandas as pd
from pydataset import data
from env import get_db_url
import acquire
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


#----------------------------------TITANIC-----------------------------------------------


def clean_titanic_data(df):
    
    df = df.drop_duplicates()

    
    cols_to_drop = ['deck', 'embarked', 'class', 'passenger_id']
    df = df.drop(columns=cols_to_drop)

    
    df['embark_town'] = df.embark_town.fillna(value='Southampton')

    
    dummy_df = pd.get_dummies(df[['sex', 'embark_town']], dummy_na=False, drop_first=[True])
    df = df.drop(columns=['sex', 'embark_town'])
    df = pd.concat([df, dummy_df], axis=1)

    return df


def split_titanic_data(df):
   
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.survived)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.survived)
    
    
    print(f'Train:{train.shape}')
    print(f'Test:{test.shape}')
    print(f'Val: {validate.shape}')
    
    print("Train Titanic Data:")
    print(train)
    print("Test Titanic Data:")
    print(test)
    print("Validation Titanic Data:")
    print(validate)

    return train, validate, test


def impute_mean_age(train, validate, test):
    
    imputer = SimpleImputer(strategy = 'mean')
    
   
    train['age'] = imputer.fit_transform(train[['age']])
    
   
    validate['age'] = imputer.transform(validate[['age']])
    
    
    test['age'] = imputer.transform(test[['age']])
    
    return train, validate, test

def prep_titanic_data(df):
    
    df = clean_titanic_data(df)

    train, validate, test = split_titanic_data(df)
    
    train, validate, test = impute_mean_age(train, validate, test)

    return train, validate, test


#----------------------------------TELCO----------------------------------------------
def prep_telco_data(df):
    df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id'], inplace=True)
       
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    
    df['total_charges'] = df.total_charges.astype(float)
    df['has_churned'] = df.churn.map({'Yes': 1, 'No': 0})
    df['gender_female'] = df.gender.map({'Female': 1, 'Male': 0})
    df['partner'] = df.partner.map({'Yes': 1, 'No': 0})
    df['dependents'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['phone_service'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['paperless_billing'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
    df['churn'] = df.churn.map({'Yes': 1, 'No': 0})
    

    
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



def split_telco_data(df):
    
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.churn)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.churn)
    
    print(f'Train:{train.shape}')
    print(f'Test:{test.shape}')
    print(f'Val: {validate.shape}')

    print("Train Telco Data:")
    print(train.shape)
    print(train)
    print("Test Telco Data:")
    print(test)
    print("Validation Telco Data:")
    print(validate)

    return train, validate, test




#--------------------------------------IRIS---------------------------------------------
def clean_iris(df):

    df = df.drop(columns='species_id')
    
    df = df.rename(columns={'species_name':'species'})
    
    dummy_df = pd.get_dummies(df['species'], drop_first=False)
    
    df = pd.concat([df, dummy_df], axis=1)
    
    return df

def split_iris_data(df):
    
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.species)
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.species)
    
    print(f'Train:{train.shape}')
    print(f'Test:{test.shape}')
    print(f'Val: {validate.shape}')

    print("Train Iris Data:")
    print(train.shape)
    print(train)
    print("Test Iris Data:")
    print(test)
    print("Validation Iris Data:")
    print(validate)

    return train, validate, test

def prep_iris_data(df):
  
    df = df.drop(columns='species_id')
    
    df = df.rename(columns={'species_name':'species'})
    
    dummy_df = pd.get_dummies(df['species'], drop_first=False)
    
    df = pd.concat([df, dummy_df], axis=1)
    
    train, validate, test = split_iris_data(df)
    
    return train, validate, test

