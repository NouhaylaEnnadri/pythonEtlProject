import pandas as pd
import os

RAW_DATA_PATH = os.path.join('data', 'raw')
PROCESSED_DATA_PATH = os.path.join('data', 'processed')

def load_raw_data(file_name):
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_name} not found in {RAW_DATA_PATH}")
    return pd.read_csv(file_path)

def filter_countries(data, countries):
    return data[data['Country Name'].isin(countries)]

def filter_years(data):
    year_columns = [str(year) for year in range(1970, 2020, 5)]
    return data[['Country Name'] + year_columns]

def remove_columns(data, columns):
    return data.drop(columns=columns)

def clean_columns(data):
    data.columns = data.columns.str.strip().str.title()
    return data

def process_temperature_data(input_file, output_file):
    raw_data = load_raw_data(input_file)
    raw_data = clean_columns(raw_data)
    filtered_data = filter_countries(raw_data, ['Algeria', 'Morocco'])
    filtered_data = remove_columns(filtered_data, ['Unit', 'Change'])
    filtered_data = filter_years(filtered_data)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    filtered_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = 'temperature_data.csv'
    output_file = os.path.join(PROCESSED_DATA_PATH, 'clean_temp.csv')
    process_temperature_data(input_file, output_file)
    print(f"Processed data saved to {output_file}")
