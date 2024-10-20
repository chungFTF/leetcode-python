# 1581-product-sales-analysis-i
import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:

    transaction_list = transactions["visit_id"].to_list()

    df = visits[~visits["visit_id"].isin(transaction_list)]
    
    df = df.groupby("customer_id").size().reset_index(name='count_no_trans')
    # print(df)
    
    return df
    
