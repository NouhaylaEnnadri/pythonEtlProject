import pandas as pd
import os

# Path to the raw data folder
RAW_DATA_PATH = os.path.join('data', 'raw')
PROCESSED_DATA_PATH = os.path.join('data', 'processed')

def load_raw_data(file_name):
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_name} not found in {RAW_DATA_PATH}")
    return pd.read_csv(file_path)

def remove_duplicates(data):
    before = data.shape[0]
    data = data.drop_duplicates()
    after = data.shape[0]
    print(f"Removed {before - after} duplicate rows.")
    return data

def handle_missing_values(data):
    # Display columns with missing data
    missing = data.isnull().sum()
    print(f"Missing values:\n{missing[missing > 0]}")

    # Example: Fill missing values in a specific column with the mean
    if 'Indicator Value' in data.columns:
        data['Indicator Value'] = data['Indicator Value'].fillna(data['Indicator Value'].mean())

    # Drop rows with missing essential columns
    data = data.dropna(subset=['Year', 'Indicator Name'])
    print(f"Remaining missing values:\n{data.isnull().sum().sum()}")
    return data

def standardize_formats(data):
    # Standardize date format
    if 'Year' in data.columns:
        data['Year'] = data['Year'].astype(int)

    # Clean numeric columns
    if 'Indicator Value' in data.columns:
        data['Indicator Value'] = pd.to_numeric(data['Indicator Value'], errors='coerce')
    return data

def normalize_text(data):
    if 'Country Name' in data.columns:
        data['Country Name'] = data['Country Name'].str.strip().str.title()

    if 'Indicator Name' in data.columns:
        data['Indicator Name'] = data['Indicator Name'].str.strip().str.lower()
    return data

def save_cleaned_data(data, file_name):
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    file_path = os.path.join(PROCESSED_DATA_PATH, file_name)
    data.to_csv(file_path, index=False)
    print(f"Cleaned data saved to {file_path}")


if __name__ == "__main__":
    raw_data = load_raw_data('climate_change_indicators.csv')
    raw_data = remove_duplicates(raw_data)
    raw_data = handle_missing_values(raw_data)
    raw_data = standardize_formats(raw_data)
    raw_data = normalize_text(raw_data)
    save_cleaned_data(raw_data, 'climate_change_indicators_cleaned.csv')

