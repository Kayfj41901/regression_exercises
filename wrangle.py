
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import env
import pandas as pd
import os
from env import host, user, password
from sklearn.model_selection import train_test_split


database_url_base = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/'

def acquire_zillow(use_cache=True):
    print('Acquiring data from SQL database')
    query = '''
        SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, propertylandusedesc, taxamount, taxvaluedollarcnt, yearbuilt, fips, transactiondate 
        FROM zillow.propertylandusetype 
        RIGHT JOIN zillow.properties_2017 
        ON propertylandusetype.propertylandusetypeid = properties_2017.propertylandusetypeid
        JOIN zillow.predictions_2017 
        ON properties_2017.parcelid = predictions_2017.parcelid
        WHERE propertylandusedesc IN ("Single Family Residential", "Inferred Single Family Residential");
         ''' 

    df = pd.read_sql(query, database_url_base + 'zillow')
    df.to_csv('wrangle_zillow.csv', index=False)
    return df

def prep_zillow(df):
    # Sort Values 
    df = df.sort_values(by='transactiondate', ascending=False)

    # Drop First Row
    df.drop(index=df.index[0], axis=0, inplace=True)

    # Drop columns propertylandusedesc and transactiondate because they were only brought in for the purpose of filtering data
    df.drop(columns=['propertylandusedesc', 'transactiondate'], inplace=True)
       
    # Drop null values  
    df = df.dropna()
    
    # Drop Outliers
    df.drop(df[df['bedroomcnt'] > 5.5].index, inplace = True)
    df.drop(df[df['bedroomcnt'] < 1.5].index, inplace = True)
    df.drop(df[df['bathroomcnt'] > 5.5].index, inplace = True)
    df.drop(df[df['bathroomcnt'] < 1].index, inplace = True)
    df.drop(df[df['calculatedfinishedsquarefeet'] > 3860].index, inplace = True)
    df.drop(df[df['taxvaluedollarcnt'] > 639679].index, inplace = True)

    # Convert columns to datatype int
    df["fips"] = df["fips"].astype(int)
    df["yearbuilt"] = df["yearbuilt"].astype(int)
    df["bedroomcnt"] = df["bedroomcnt"].astype(int)
    df["taxvaluedollarcnt"] = df["taxvaluedollarcnt"].astype(int)
    df["calculatedfinishedsquarefeet"] = df["calculatedfinishedsquarefeet"].astype(int)
    df["taxamount"] = df["taxamount"].astype(int)

    #map fips to location
    df['location'] = df.fips.map({6037:'LA', 6059:'Orange', 6111:'Ventura'})

    #drop columns
    df.drop(columns=['fips'], inplace=True)
    return df

def wrangle_zillow(): 
    """
    Acquires Zillow data from SQL 
    Sorts values 
    Drops Rows
    Drops Columns 
    Drops null types
    Drops Outliers calculated using 1.5 * IQR method 
    Converts 5 column datatypes to int
    """
    df = acquire_zillow(use_cache = True)

    df = prep_zillow(df)

    return df

def split_zillow_data(df):
    '''
    This function performs split on zillow data
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123)
    return train, validate, test

 
def scale_data(train, 
               validate, 
               test, 
               columns_to_scale=['bedroomcnt', 'bathroomcnt', 'calculatedfinishedsquarefeet'],
               return_scaler=False):
    '''
    Scales the 3 data splits. 
    Takes in train, validate, and test data splits and returns their scaled counterparts.
    If return_scalar is True, the scaler object will be returned as well
    '''
    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()
    
    scaler = MinMaxScaler()
    scaler.fit(train[columns_to_scale])
    
    train_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(train[columns_to_scale]),
                                                  columns=train[columns_to_scale].columns.values).set_index([train.index.values])
                                                  
    validate_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(validate[columns_to_scale]),
                                                  columns=validate[columns_to_scale].columns.values).set_index([validate.index.values])
    
    test_scaled[columns_to_scale] = pd.DataFrame(scaler.transform(test[columns_to_scale]),
                                                 columns=test[columns_to_scale].columns.values).set_index([test.index.values])
    
    if return_scaler:
        return scaler, train_scaled, validate_scaled, test_scaled
    else:
        return train_scaled, validate_scaled, test_scaled
