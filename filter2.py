import pandas as pd

# Load your existing CSV data into a DataFrame
df = pd.read_csv('4p1.csv')

# Define a function to adjust speed based on datetime conditions
def adjust_speed(row):
    datetime = pd.to_datetime(row['datetime'])
    speed = row['average_speed']


    # if datetime.time() > pd.to_datetime('05:00:00').time() and datetime.time() <= pd.to_datetime('07:30:00').time():
    #     # if speed > 32:
    #     #     return speed - 2
    #     # elif speed <7:
    #     #     return speed + 7
    #     return speed +15
    # elif datetime.time() > pd.to_datetime('07:30:00').time() and datetime.time() <= pd.to_datetime('10:30:00').time():
    #     # if speed > 30:
    #     #     return speed - 4
    #     # elif speed <7:
    #     #     return speed + 5
    #     return speed +10
    if datetime.time() > pd.to_datetime('5:00:00').time() and datetime.time() <= pd.to_datetime('8:40:00').time():
        # if speed < 30:
        #     return speed - 5
        # elif speed <7:
            return speed +5
        # return speed +3
    # elif datetime.time() > pd.to_datetime('12:25:00').time() and datetime.time() <= pd.to_datetime('15:25:00').time():
    #     # if speed > 30:
    #     #     return speed - 5
    #     # elif speed <7:
    #     #     return speed + 3
    #     return speed +10
    # elif datetime.time() > pd.to_datetime('15:25:00').time() and datetime.time() <= pd.to_datetime('18:30:00').time():
    #     # if speed > 30:
    #     #     return speed - 5
    #     # elif speed <7:
    #     #     return speed + 3
    #     return speed +0
    
    return speed  # Default to original speed if no conditions are met

# Apply the function to adjust speeds and update the average_speed column
df['average_speed'] = df.apply(adjust_speed, axis=1)

# Save the modified DataFrame back to the original CSV file
# df = df[pd.to_datetime(df['datetime']).dt.time <= pd.to_datetime('19:00:00').time()]
# df['time'] = pd.to_datetime(df['datetime']).dt.time

# # Sort by the extracted time
# df_sorted = df.sort_values(by=['road_segment','time'])
# df_sorted = df_sorted.drop(columns=['time'])
df.to_csv('4p1.csv', index=False)
