# 1378-replace-employee-id-with-the-unique-identifier
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    
    df = pd.merge(employees,employee_uni, how="left")[["unique_id","name"]]
    # print(df)

    return df