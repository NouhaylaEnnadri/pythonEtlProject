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

def remove_columns(data):
    # Remove unwanted columns
    columns_to_drop = ['Iso2', 'Iso3', 'Indicator', 'Unit', 'Source', 
                       'Cts_Code', 'Cts_Name', 'Cts_Full_Descriptor']
    data = data.drop(columns=columns_to_drop, errors='ignore')
    return data

def filter_countries(data, countries):
    # Filter rows for the specified countries (e.g., Algeria and Morocco)
    filtered_data = data[data['Country'].isin(countries)]
    return filtered_data

def filter_years(data):
    # Extract columns for years from F1961 to F2022
    year_columns = [f'F{i}' for i in range(1961, 2023)]
    data = data[['Country'] + year_columns]  # Include 'Country' and year columns
    return data

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
    data = data.dropna(subset=['Country'])
    print(f"Remaining missing values:\n{data.isnull().sum().sum()}")
    return data

def save_cleaned_data(data, file_name):
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    file_path = os.path.join(PROCESSED_DATA_PATH, file_name)
    data.to_csv(file_path, index=False)
    print(f"Cleaned data saved to {file_path}")

if __name__ == "__main__":
    # Load raw data
    raw_data = load_raw_data('climate_change_indicators.csv')
    
    # Clean up column names (strip spaces and standardize case)
    raw_data.columns = raw_data.columns.str.strip().str.title()
    
    # Print the columns to check if 'Country' exists
    print("Columns in dataset:", raw_data.columns)

    # Filter for the specified countries (Algeria and Morocco)
    filtered_data = filter_countries(raw_data, ['Algeria', 'Morocco'])
    
    # Filter for the required columns (Year columns only)
    filtered_data = filter_years(filtered_data)
    
    # Remove unwanted columns
    filtered_data = remove_columns(filtered_data)
    
    # Apply transformations
    filtered_data = remove_duplicates(filtered_data)
    filtered_data = handle_missing_values(filtered_data)
    
    # Display the final filtered and cleaned data
    print("Filtered and cleaned data:\n", filtered_data.head())  # Display first 5 rows for preview
    
    # Optionally: Save the cleaned data
    save_cleaned_data(filtered_data, 'climate_change_indicators_cleaned.csv')
