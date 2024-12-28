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

# Run the function to fetch the data
df, metadata = download_co2_data()


# Define the path where the data will be saved
save_path = 'C:/Users/SWIFT 3/pythonEtlProject/data/raw/co2_emissions.csv'

# Check if the directory exists, if not, create it
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the DataFrame as a CSV file in the 'data/raw' directory
df.to_csv(save_path, index=False)
