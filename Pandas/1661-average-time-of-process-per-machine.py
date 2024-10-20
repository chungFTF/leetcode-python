# 1661-average-time-of-process-per-machine
import pandas as pd

# Sol 2
def get_average_time(df: pd.DataFrame) -> pd.DataFrame:

    data = df.pivot(index=["machine_id", "process_id"], columns=["activity_type"], values="timestamp")
    data["processing_time"] = data["end"] - data["start"]

    return data.groupby("machine_id")["processing_time"].mean().round(3).reset_index()



# Sol 1
# def get_average_time(df: pd.DataFrame) -> pd.DataFrame:
#     df_start = df[df["activity_type"] == "start"]
#     df_end = df[df["activity_type"] == "end"]

#     new_df = pd.merge(df_start, df_end, on=["machine_id", "process_id"])
#     new_df["processing_time"] = new_df["timestamp_y"] - new_df["timestamp_x"]

#     new_df = new_df.groupby("machine_id")["processing_time"].mean().round(3).reset_index()

#     return new_df


