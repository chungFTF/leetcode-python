# 1148-article-views-i


import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    # df = views[views["author_id"] == views["viewer_id"]][["author_id"]].drop_duplicates().sort_values(by="author_id")

    df = views[views["author_id"] == views["viewer_id"]]["author_id"].unique()
    # print(df)
    result_df = pd.DataFrame({'id': sorted(df)})

    return result_df