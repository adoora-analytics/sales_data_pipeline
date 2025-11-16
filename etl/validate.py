def validate(df):
    null_count = df.isnull().sum().sum()

    assert null_count == 0, f"Null values found! Total nulls: {null_count}"
    assert len(df) > 0, "No rows loaded!"  
    return True