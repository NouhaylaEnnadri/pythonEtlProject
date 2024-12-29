import pandas as pd
import requests
import os

def download_co2_data():
    # Data URL
    data_url = "https://ourworldindata.org/grapher/annual-co2-emissions-per-country.csv?v=1&csvType=full&useColumnShortNames=true"

    # Fetch the data using Pandas
    df = pd.read_csv(data_url, storage_options={'User-Agent': 'Our World In Data data fetch/1.0'})

    # Fetch metadata (optional)
    metadata_url = "https://ourworldindata.org/grapher/annual-co2-emissions-per-country.metadata.json?v=1&csvType=full&useColumnShortNames=true"
    metadata = requests.get(metadata_url).json()

    # Return the data and metadata
    return df, metadata

def load_raw_data(file_path):
    # Load the CO2 dataset from a CSV file
    return pd.read_csv(file_path)

def filter_countries(data, countries):
    # Filter the data for the specified countries
    return data[data['Entity'].isin(countries)]

def filter_years(data, start_year, end_year):
    # Filter the data for the years between start_year and end_year
    years = [str(year) for year in range(start_year, end_year + 1)]
    return data[['Entity', 'Code'] + years]

# Run the function to fetch the data
df, metadata = download_co2_data()

# Define the path where the data will be saved
save_path = 'C:/Users/SWIFT 3/pythonEtlProject/data/raw/co2_emissions.csv'

# Check if the directory exists, if not, create it
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the DataFrame as a CSV file in the 'data/raw' directory
df.to_csv(save_path, index=False)
