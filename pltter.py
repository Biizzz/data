
# import pandas as pd
# import matplotlib.pyplot as plt

# # Read the CSV file
# df = pd.read_csv('6p1.csv')

# # Drop any rows with missing values in critical columns
# df.dropna(subset=['datetime', 'average_speed'], inplace=True)

# # Convert datetime column to pandas datetime
# df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')

# # Drop any rows where datetime conversion resulted in NaT
# df = df.dropna(subset=['datetime'])

# # Extract hour and minute for grouping
# df['hour'] = df['datetime'].dt.hour
# df['minute'] = df['datetime'].dt.minute

# # Create a time interval column for 15-minute intervals
# df['time_interval'] = df['hour'] * 6 + df['minute'] // 10

# # Define a function to calculate congestion index
# def calculate_congestion(speed, max_speed=60):
#     return max(0, min(1, 1 - (speed / max_speed)))

# # Calculate congestion index
# df['congestion_index'] = df['average_speed'].apply(calculate_congestion)

# # Group by time interval and calculate the mean congestion index
# grouped = df.groupby('time_interval')['congestion_index'].mean().reset_index()

# # Convert the time interval back to a readable format
# grouped['time_of_day'] = (grouped['time_interval'] // 6).astype(str).str.zfill(2) + ':' + ((grouped['time_interval'] % 6) * 10).astype(str).str.zfill(2)

# # Plot bar chart
# plt.figure(figsize=(16, 8))
# plt.bar(grouped['time_of_day'], grouped['congestion_index'], color='salmon', edgecolor='black')
# plt.xlabel('Time of Day')
# plt.ylabel('Congestion Index')
# plt.title('Congestion vs. Time of Day')
# plt.xticks(rotation=90)
# plt.ylim(0, 1)
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('4p1.csv')

# Drop any rows with missing values in critical columns
df.dropna(subset=['datetime', 'average_speed'], inplace=True)

# Convert datetime column to pandas datetime
df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')

# Drop any rows where datetime conversion resulted in NaT


# Extract hour and minute for grouping
df['hour'] = df['datetime'].dt.hour
df['minute'] = df['datetime'].dt.minute

# Create a time interval column for 15-minute intervals
df['time_interval'] = df['hour'] * 6 + df['minute'] // 10

# Define a function to categorize congestion
def categorize_congestion(speed):
    if speed > 30:
        return "Free Flow"
    elif 20 < speed <= 30:
        return "Light Traffic"
    elif 10 < speed <= 20:
        return "Moderate Traffic"
    elif 5 < speed <= 10:
        return "Heavy Traffic"
    else:
        return "Severe Congestion"

# Categorize congestion
df['congestion_category'] = df['average_speed'].apply(categorize_congestion)

# Group by time interval and calculate the most frequent congestion category
grouped = df.groupby('time_interval')['congestion_category'].agg(lambda x: x.mode()[0]).reset_index()

# Convert the time interval back to a readable format
grouped['time_of_day'] = (grouped['time_interval'] // 6).astype(str).str.zfill(2) + ':' + ((grouped['time_interval'] % 6) * 10).astype(str).str.zfill(2)

# Plot bar chart
plt.figure(figsize=(16, 8))
plt.bar(grouped['time_of_day'], grouped['congestion_category'].map({
    "Free Flow": 1,
    "Light Traffic": 2,
    "Moderate Traffic": 3,
    "Heavy Traffic": 4,
    "Severe Congestion": 5
}), color='salmon', edgecolor='black')
plt.xlabel('Time of Day')
plt.ylabel('Congestion Category')
plt.title('Congestion vs. Time of Day')
plt.xticks(rotation=90)
plt.yticks([1, 2, 3, 4, 5], ['Free Flow', 'Light Traffic', 'Moderate Traffic', 'Heavy Traffic', 'Severe Congestion'])
plt.ylim(0.5, 5.5)
plt.show()
