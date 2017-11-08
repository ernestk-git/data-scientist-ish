# takes a pandas dataframe and shrinks to smallest datatype
def data_shrinker(df, verbose=False):
    num_cols = len(df.columns)
    for i in range(num_cols):
        if verbose:
            print('Column: %s of %s' % (i, num_cols))
        if 'float' in str(df.iloc[:,i].dtype):
            df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], downcast='float')
        elif 'int' in str(df.iloc[:,i].dtype):
             df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], downcast='integer')

    return df
