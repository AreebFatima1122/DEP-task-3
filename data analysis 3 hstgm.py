import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/storage/emulated/0/Download/Cars.csv')

# Display the first few rows of the dataframe
print(df.head())

# Histogram of 'Horsepower'
plt.figure(figsize=(10, 6))
plt.hist(df['Horsepower'].dropna(), bins=20, edgecolor='black')
plt.title('Distribution of Horsepower')
plt.xlabel('Horsepower')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Histogram of 'Miles_per_Gallon'
plt.figure(figsize=(10, 6))
plt.hist(df['Miles_per_Gallon'].dropna(), bins=20, edgecolor='black')
plt.title('Distribution of Miles per Gallon')
plt.xlabel('Miles per Gallon')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
