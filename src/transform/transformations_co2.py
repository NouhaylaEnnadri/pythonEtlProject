import pandas as pd
import os

RAW_DATA_PATH = os.path.join('data', 'raw')

def load_raw_data(file_name):
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_name} not found in {RAW_DATA_PATH}")
    return pd.read_csv(file_path)

def filter_countries(data, countries):
    return data[data['Entity'].isin(countries)]

def filter_years(data, start_year=1960, end_year=2022):
    return data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]

def remove_columns(data, columns):
    return data.drop(columns=columns)

def clean_columns(data):
    data.columns = data.columns.str.strip().str.title()
    return data

if __name__ == "__main__":
    # Example usage
    raw_data = load_raw_data('co2_emissions.csv')
    raw_data = clean_columns(raw_data)
    
    # Filter for Morocco and Algeria
    filtered_data = filter_countries(raw_data, ['Morocco', 'Algeria'])
    
    # Filter for years from 1960 to 2022
    filtered_data = filter_years(filtered_data)
    
    # Remove unnecessary columns
    filtered_data = remove_columns(filtered_data, ['Code'])  # Code column is not needed
    
    print(filtered_data.head())
