import pandas as pd
import matplotlib.pyplot as plt

# Load dataset from URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Count species
print("\nSpecies Count:")
print(df['species'].value_counts())

# Simple visualization
plt.scatter(df['sepal_length'], df['petal_length'])
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()