import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.lower().str.strip()
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df


