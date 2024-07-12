import pandas as pd
import os

# Read the CSV file
data = pd.read_csv('op.csv')

# Separate the data by road segments and save them as different files
for segment in range(8):
    segment_data = data[data['road_segment'] == segment]
    segment_data.to_csv(f"{segment}.csv", index=False)
