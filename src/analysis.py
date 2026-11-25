import pandas as pd

# Read the CSV file
data = pd.read_csv("data/chilli_observations.csv")

# Display the dataset
print("CHILLI DRYING OBSERVATIONS")
print(data)

# Display first five rows
print("\nFirst five observations:")
print(data.head())

# Display dataset information
print("\nDataset information:")
data.info()

# Calculate average temperature
avg_temperature = data["temperature"].mean()

# Calculate average moisture
avg_moisture = data["moisture"].mean()

print("\nAverage temperature:", avg_temperature)
print("Average moisture:", avg_moisture)
# Total number of observations
print("\nTotal observations:", len(data))

# Number of rows and columns
print("Dataset shape:", data.shape)

# Moisture readings at 6 hours
six_hour_data = data[data["drying_hours"] == 6]

print("\nObservations at 6 hours:")
print(six_hour_data)

# Batch with lowest moisture at 6 hours
lowest_batch = six_hour_data.loc[
    six_hour_data["moisture"].idxmin()
]

print("\nLowest moisture batch:")
print(lowest_batch)

highest_temperature_batch= data.loc[data["temperature"].idxmax()]
print("\nHighest temperature batch:")
print(highest_temperature_batch)

lowest_humidity_batch=data.loc[data["humidity"].idxmin()]
print("\nLowest humidity batch:")
print(lowest_humidity_batch)

print(data.groupby("batch_id")["moisture"].mean())

# Check missing values
print("\nMissing values:")
print(data.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:")
print(data.duplicated().sum())

# Check unique batches
print("\nAvailable batches:")
print(data["batch_id"].unique())