import pandas as pd
import os

# Adjusted path to go up two levels from the current directory to access data/raw and data/processed
RAW_DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')
PROCESSED_DATA_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'processed')

def load_raw_data(file_name):
    # Create the full file path
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    
    # Print out the file path for debugging purposes
    print(f"Looking for file at: {file_path}")
    
    # Check if the file exists at the specified path
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_name} not found in {RAW_DATA_PATH}")
    
    return pd.read_csv(file_path)

def filter_countries(data, countries=None):
    # If countries is empty or None, we return all countries
    if countries:
        return data[data['Entity'].isin(countries)]
    return data

def filter_years(data, start_year=1960, end_year=2022):
    return data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]

def remove_columns(data, columns):
    return data.drop(columns=columns)

def clean_columns(data):
    # Clean column names by stripping spaces and capitalizing first letters
    data.columns = data.columns.str.strip().str.title()
    return data

def save_processed_data(data, file_name):
    # Save the processed data to the specified directory (../../data/processed)
    processed_file_path = os.path.join(PROCESSED_DATA_PATH, file_name)
    
    # Ensure the processed directory exists
    if not os.path.exists(PROCESSED_DATA_PATH):
        os.makedirs(PROCESSED_DATA_PATH)
    
    # Save the dataframe to a CSV file
    data.to_csv(processed_file_path, index=False)
    print(f"Processed data saved to: {processed_file_path}")

if __name__ == "__main__":
    try:
        # Load the raw data
        raw_data = load_raw_data('co2_emissions.csv')
        
        # Clean column names
        raw_data = clean_columns(raw_data)
        
        # Example: Filter for countries or all countries (empty list means all countries)
        filtered_data = filter_countries(raw_data, [])
        
        # Filter for years from 1960 to 2022
        filtered_data = filter_years(filtered_data)
        
        # Optional: Remove unnecessary columns (if needed)
        # filtered_data = remove_columns(filtered_data, ['Code'])  # Uncomment if needed
        
        # Save the processed data to the processed folder
        save_processed_data(filtered_data, 'cleaned_co2_emissions.csv')
    
    except Exception as e:
        print(f"An error occurred: {e}")
