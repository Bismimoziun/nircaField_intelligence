
import pandas as pd

# Load the dataset
data = pd.read_csv("data/chilli_observations.csv")

# Display descriptive statistics
print("DESCRIPTIVE STATISTICS")
print(data.describe())

# Display correlation between numerical columns
print("\nCORRELATION MATRIX")
print(data.corr(numeric_only=True))


import matplotlib.pyplot as plt

# Graph 1: Drying hours vs moisture
plt.figure(figsize=(8, 5))

plt.scatter(
    data["drying_hours"],
    data["moisture"]
)

plt.xlabel("Drying Hours")
plt.ylabel("Moisture")
plt.title("Drying Hours vs Moisture")

plt.grid(True)
plt.show()

plt.scatter(data["temperature"], data["moisture"])

plt.xlabel("Temperature")
plt.ylabel("Moisture")
plt.title("Temperature vs Moisture")

plt.show()

plt.scatter(data["temperature"], data["moisture"])

plt.xlabel("Temperature")
plt.ylabel("Moisture")
plt.title("Temperature vs Moisture")

plt.show()