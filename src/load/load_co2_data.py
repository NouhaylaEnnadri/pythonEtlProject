import os
import sqlite3
import pandas as pd

# Step 1: Define paths
BASE_DATA_DIR = os.path.join("..", "..", "data")
DATABASE_DIR = os.path.join(BASE_DATA_DIR, "sqliteDatabase")
os.makedirs(DATABASE_DIR, exist_ok=True)  # Create the database directory if it doesn't exist

DATABASE_PATH = os.path.join(DATABASE_DIR, "co2_emissions.db")

# Step 2: Function to drop the table if it exists
def drop_table_if_exists(conn, table_name):
    drop_table_query = f"DROP TABLE IF EXISTS {table_name};"
    try:
        cursor = conn.cursor()
        cursor.execute(drop_table_query)
        print(f"Table '{table_name}' dropped (if it existed).")
    except Exception as e:
        print(f"Error dropping table: {e}")

# Step 3: Function to create a table with the correct schema
def create_table(conn, table_name):
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        Entity TEXT,
        Code TEXT,
        Year INTEGER,
        Emissions_Total REAL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")

# Step 4: Function to load CSV data into the database
def load_data_to_db(csv_file_path, table_name):
    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file not found at: {csv_file_path}")
    
    # Connect to SQLite database
    conn = sqlite3.connect(DATABASE_PATH)
    print(f"Connected to database at {DATABASE_PATH}")

    try:
        # Drop the table if it exists
        drop_table_if_exists(conn, table_name)
        
        # Create the table with the correct schema
        create_table(conn, table_name)
        
        # Load CSV data into a DataFrame
        data = pd.read_csv(csv_file_path)
        print(f"Loaded {len(data)} rows from {csv_file_path}")
        
        # Insert data into the table
        data.to_sql(table_name, conn, if_exists="append", index=False)
        print(f"Data successfully loaded into table: {table_name}")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        # Close the database connection
        conn.close()
        print("Database connection closed.")

# Step 5: Main block for execution
if __name__ == "__main__":
    # Define the path to the raw CSV file
    RAW_CSV_PATH = os.path.join(BASE_DATA_DIR, "processed", "cleaned_co2_emissions.csv")
    
    # Define the table name in the database
    TABLE_NAME = "co2_emissions"
    
    # Call the function to load data into the database
    load_data_to_db(RAW_CSV_PATH, TABLE_NAME)
