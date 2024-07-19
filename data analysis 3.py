import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/storage/emulated/0/Download/Cars.csv')

# Display the first few rows of the dataframe
print(df.head())

# Scatter plot of 'horsepower' vs 'miles per gallon'
plt.figure(figsize=(10, 6))
plt.scatter(df['Horsepower'], df['Miles_per_Gallon'], alpha=0.5)
plt.title('Horsepower vs. Miles_per_Gallon')
plt.xlabel('Horsepower')
plt.ylabel('Miles_per_Gallon')
plt.grid(True)
plt.show()


