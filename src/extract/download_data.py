# src/extract/download_data.py
#This script handles downloading the Kaggle dataset and saving it to the raw data directory.
import kaggle
import os

def download_kaggle_dataset():
    # Authenticate with Kaggle
    kaggle.api.authenticate()

    # Define dataset and destination
    dataset_name = 'tarunrm09/climate-change-indicators'
    destination_path = os.path.join('data', 'raw')

    # Ensure the destination directory exists
    os.makedirs(destination_path, exist_ok=True)

    # Download the dataset and unzip it
    kaggle.api.dataset_download_files(dataset_name, path=destination_path, unzip=True)
    print(f"Dataset downloaded and saved to {destination_path}")

if __name__ == "__main__":
    download_kaggle_dataset()
