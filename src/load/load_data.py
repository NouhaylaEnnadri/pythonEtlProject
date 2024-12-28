import os
import pandas as pd
import sqlite3  # Using SQLite as an example

# Define paths
PROCESSED_DATA_PATH = os.path.join('data', 'processed')
DATABASE_PATH = os.path.join('data', 'climate_data.db')  # Path for SQLite database

def load_into_database(file_name):
    """
    Loads the processed dataset into a SQLite database.
    """
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Load processed dataset
    processed_file_path = os.path.join(PROCESSED_DATA_PATH, file_name)
    if not os.path.exists(processed_file_path):
        raise FileNotFoundError(f"{file_name} not found in {PROCESSED_DATA_PATH}")

    df = pd.read_csv(processed_file_path)

    # Write data to the database
    table_name = 'climate_data'
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Data loaded into table '{table_name}' in {DATABASE_PATH}")

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    # Replace with the actual processed file name
    processed_file_name = 'cleaned_climate_change_indicators.csv'
    load_into_database(processed_file_name)
