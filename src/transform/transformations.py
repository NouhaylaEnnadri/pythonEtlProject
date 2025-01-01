# transformations.py

import pandas as pd
import os

# Path to the raw data folder
RAW_DATA_PATH = os.path.join('data', 'raw')

# Load the data (already filtered for Algeria and Morocco)
def load_raw_data(file_name):
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_name} not found in {RAW_DATA_PATH}")
    return pd.read_csv(file_path)

def filter_countries(data, countries):
    # Filter rows for the specified countries (e.g., Algeria and Morocco)
    filtered_data = data[data['Country'].isin(countries)]
    return filtered_data

def filter_years(data):
    # Extract columns for years from F1961 to F2022
    year_columns = [f'F{i}' for i in range(1970, 2020)]
    data = data[['Country'] + year_columns]  # Include 'Country' and year columns
    return data

# Main data processing function
def process_data(file_name, countries):
    # Load raw data
    raw_data = load_raw_data(file_name)
    
    # Clean up column names (strip spaces and standardize case)
    raw_data.columns = raw_data.columns.str.strip().str.title()
    
    # Filter for the specified countries (Algeria and Morocco)
    filtered_data = filter_countries(raw_data, countries)
    
    # Filter for the required columns (Year columns only)
    filtered_data = filter_years(filtered_data)
    
    return filtered_data
