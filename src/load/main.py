# src/load/main.py
#This script loads a dataset file from the raw data folder into a Pandas DataFrame for further processing
import os
import pandas as pd

# Path to the raw data folder
RAW_DATA_PATH = os.path.join('data', 'raw')

def load_dataset(file_name):
    """Loads the dataset into a DataFrame."""
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_name} not found in {RAW_DATA_PATH}")
    
    # Assuming the dataset is in CSV format
    df = pd.read_csv(file_path)
    print(f"Dataset loaded successfully: {file_name}")
    return df

def main():
    # Example usage
    dataset_file_name = 'climate_change_indicators.csv'  # Replace with the actual file name
    try:
        df = load_dataset(dataset_file_name)
        print(df.head())  # Display the first few rows of the dataset
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
