import pandas as pd
from pathlib import Path

# Load dataset
file_path = Path("data/raw/SampleSuperstore.csv")
df = pd.read_csv(file_path)

# Display information
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Remove duplicates
print("\nDuplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Save cleaned data
output_path = Path("data/processed/cleaned_sales.csv")
df.to_csv(output_path, index=False)

print("\n✅ Data cleaned successfully!")