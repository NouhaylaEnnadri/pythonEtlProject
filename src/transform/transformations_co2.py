import pandas as pd
import os

# Adjusted paths to go up two levels from the current directory to access data/raw and data/processed
RAW_DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')
PROCESSED_DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'processed')

def load_raw_data(file_name):
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    print(f"Looking for file at: {file_path}")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_name} not found in {RAW_DATA_PATH}")
    return pd.read_csv(file_path)

def filter_countries(data, countries):
    return data[data['Entity'].isin(countries)]

def filter_years(data, start_year, end_year):
    return data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]

def remove_columns(data, columns):
    return data.drop(columns=columns)

def clean_columns(data):
    data.columns = data.columns.str.strip().str.title()
    return data

def save_processed_data(data, file_name):
    processed_file_path = os.path.join(PROCESSED_DATA_PATH, file_name)
    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)
    data.to_csv(processed_file_path, index=False)
    print(f"Processed data saved to: {processed_file_path}")

if __name__ == "__main__":
    try:
        # Load the raw data
        raw_data = load_raw_data('co2_emissions.csv')
        
        # Clean column names
        raw_data = clean_columns(raw_data)
        
        # Filter for Morocco and Algeria
        filtered_data = filter_countries(raw_data, ['Morocco', 'Algeria'])
        
        # Filter for years between 1960 and 2022
        filtered_data = filter_years(filtered_data, 1970, 2020)
        
        # Remove the Code column
        filtered_data = remove_columns(filtered_data, ['Code'])
        
        # Save the processed data
        save_processed_data(filtered_data, 'cleaned_co2_emissions.csv')
    
    except Exception as e:
        print(f"An error occurred: {e}")
