def isPrimaryKey(df, columnList):
    """
    returns True if the set of columns is a primary key of the DataFrame
    
    args
        df: The DataFrame to test
        columnList: a list of columns
        
    returns
        boolean
    """
    # we test if each columns given exist in df
    for columnInput in columnList:
        if columnInput not in df.columns:
            raise ValueError("'{}' is not a valid column".format(columnInput))
    
    # --> is there two identic lines when we project df ?
    # we project df into the given columns
    # we delete the duplicates of the projection
    # we count the number of line and compare it to the initial one
    return len(df) == len(df.drop_duplicates(subset=columnList))
    
def chunk_df(df, chunk_size=100):
    """
    this method chunk a dataframe into sub DataFrame.
    the function will reset the row index (from 0 to len(df))
    
    Parameters
    ----------
    df : the dataframe to chunk
    chunk_size: the maximum number of rows per chunks
    
    Returns
    -------
    an array of DataFrame, each is a chunk of the input one
    
    """
    # we reset the row index from 0 to len(df)
    df.reset_index(drop=True, inplace=True)
    # we create a list which contains the chunks of df
    return [df[i:i+chunk_size] for i in range(0, df.shape[0], chunk_size)]