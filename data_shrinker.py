import pandas as pd 

# takes a pandas dataframe and shrinks to smallest datatype
def data_shrinker(df):
    num_cols = len(train_data.columns)
    for i in range(num_cols):
        if 'float' in str(df.iloc[:,i].dtype):
            df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], downcast='float')
        elif 'int' in str(df.iloc[:,i].dtype):
             df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], downcast='integer')
