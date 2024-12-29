import pandas as pd
import requests
import os

RAW_DATA_PATH = os.path.join('../../data', 'raw')  # Directory to save raw data
CO2_DATA_FILE = os.path.join(RAW_DATA_PATH, 'co2_emissions.csv')

def Extract_co2_data():
    """
    Download CO2 emissions data from Our World in Data and save it locally.
    """
    # URL for the data
    data_url = "https://ourworldindata.org/grapher/annual-co2-emissions-per-country.csv?v=1&csvType=full&useColumnShortNames=true"
    metadata_url = "https://ourworldindata.org/grapher/annual-co2-emissions-per-country.metadata.json?v=1&csvType=full&useColumnShortNames=true"

    # Fetch the data
    print("Downloading CO2 emissions data...")
    df = pd.read_csv(data_url, storage_options={'User-Agent': 'Our World In Data data fetch/1.0'})
    
    # Fetch metadata (optional)
    print("Downloading metadata...")
    metadata = requests.get(metadata_url).json()

    # Ensure raw data directory exists
    os.makedirs(RAW_DATA_PATH, exist_ok=True)

    # Save the data locally
    print(f"Saving data to {CO2_DATA_FILE}...")
    df.to_csv(CO2_DATA_FILE, index=False)

    # Return the downloaded data for immediate use
    return df, metadata

if __name__ == "__main__":
    # Run the extraction step
    df, metadata = Extract_co2_data()
    print("Data extraction completed!")
