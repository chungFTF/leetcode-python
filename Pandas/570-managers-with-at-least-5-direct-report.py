# 570-managers-with-at-least-5-direct-report
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    df = employee.groupby("managerId").size() >= 5
    true_indices = df[df].index
    results = employee[employee["id"].isin(true_indices)][["name"]]
    # print(results)
    return results


