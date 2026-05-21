def assert_columns(df, required_columns):
    """
    Validate that required columns
    exist in the dataframe.
    """
    missing_cols = [col for col in required_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(
            f"Missing columns: {missing_cols}")
    print("All required columns are present.")
    
    
def print_dataframe_shape(df):
    """
    Print dataframe dimensions.
    """
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
