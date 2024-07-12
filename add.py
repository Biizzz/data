import pandas as pd
import os

# Read the CSV file
df = pd.read_csv('op.csv')

# Add 10 to the average_speed column
df['average_speed'] = df['average_speed'] + 10

# Save the modified DataFrame to a new CSV file
df.to_csv("op1.csv", index=False)
