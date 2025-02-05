# 1068-product-sales-analysis-i
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(sales,product, on="product_id", how="inner")
    # print(df)

    return df[["product_name", "year", "price"]]
    
    