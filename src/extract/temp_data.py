import kaggle
import os
import zipfile

def download_kaggle_dataset():
    # Authenticate with Kaggle
    kaggle.api.authenticate()

    # Define dataset and destination
    dataset_name = 'mdazizulkabirlovlu/all-countries-temperature-statistics-1970-2021'
    destination_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data', 'raw')

    # Ensure the destination directory exists
    os.makedirs(destination_path, exist_ok=True)

    # Download the dataset (it will be a ZIP file)
    kaggle.api.dataset_download_files(dataset_name, path=destination_path, unzip=False)

    # Locate the downloaded zip file
    downloaded_file = os.path.join(destination_path, f"{dataset_name.split('/')[-1]}.zip")

    # Unzip the file and rename the CSV to 'test.csv'
    with zipfile.ZipFile(downloaded_file, 'r') as zip_ref:
        zip_ref.extractall(destination_path)  # Extract all files in the destination path
        
        # Find the CSV file in the extracted files
        for filename in zip_ref.namelist():
            if filename.endswith('.csv'):
                # Rename the CSV to 'test.csv'
                csv_file_path = os.path.join(destination_path, filename)
                new_csv_name = os.path.join(destination_path, 'temperature_data.csv')
                os.rename(csv_file_path, new_csv_name)
                print(f"CSV file extracted and renamed to {new_csv_name}")
                break

    # Remove the original ZIP file after extraction (optional)
    os.remove(downloaded_file)

    # Optional: Check if the files are properly downloaded and unzipped
    print("Files in the destination folder:")
    for filename in os.listdir(destination_path):
        print(f"  - {filename}")

if __name__ == "__main__":
    download_kaggle_dataset()
