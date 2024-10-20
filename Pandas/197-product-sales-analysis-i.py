# 197-product-sales-analysis-i
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    
    weather = weather.sort_values(by='recordDate')
    temp_diff = weather['temperature'].diff()
    date_diff = weather['recordDate'].diff().dt.days

    diff_results = weather[(temp_diff > 0) & (date_diff == 1)][["id"]]
    print(diff_results)
    return diff_results
