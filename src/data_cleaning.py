import pandas as pd

# Load original dataset
data = pd.read_csv("data/chilli_observations.csv")

# Create a practice copy
dirty_data = data.copy()

# Introduce a missing value
dirty_data.loc[1, "temperature"] = None

# Introduce a duplicate row
dirty_data = pd.concat(
    [dirty_data, dirty_data.iloc[[0]]],
    ignore_index=True
)

print("PRACTICE DATA")
print(dirty_data)

# Check missing values
print("\nMissing values:")
print(dirty_data.isnull().sum())

# Check duplicate rows
print("\nDuplicate count:")
print(dirty_data.duplicated().sum())

# Handle missing temperature using column mean
dirty_data["temperature"] = dirty_data["temperature"].fillna(
    dirty_data["temperature"].mean()
)

# Remove exact duplicate rows
dirty_data = dirty_data.drop_duplicates()

print("\nCLEANED DATA")
print(dirty_data)

print("\nFinal missing values:")
print(dirty_data.isnull().sum())

print("\nFinal duplicate count:")
print(dirty_data.duplicated().sum())