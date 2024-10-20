# 1683-invalid-tweets
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    
    df = tweets[tweets["content"].str.len() > 15]
    # print(df)

    return df[["tweet_id"]]