# takes a pandas dataframe and shrinks to smallest datatype
def data_shrinker(df, verbose=False):
    # Iterate over columns, and change them out
    for i in range(len(df.columns)):
        if verbose:
            print('Column: %s of %s' % (i, num_cols))
        if 'float' in str(df.iloc[:,i].dtype):
            df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], downcast='float')
        elif 'int' in str(df.iloc[:,i].dtype):
             df.iloc[:,i] = pd.to_numeric(df.iloc[:,i], downcast='integer')

    return df
