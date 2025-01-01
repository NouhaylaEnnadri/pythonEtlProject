import pandas as pd

def clean_health_data(file_path, countries=None):
    # Load the dataset
    health_data = pd.read_csv(file_path)
    
    # Remove extra spaces from column names
    health_data.columns = health_data.columns.str.strip()
    
    # If countries are provided, filter by those countries, otherwise include all
    if countries:
        filtered_data = health_data[health_data['Entity'].isin(countries)]
    else:
        filtered_data = health_data  # Include all countries if no filter is applied
    
    # Filter for years between 1960 and 2022
    filtered_data = filtered_data[(filtered_data['Year'] >= 1960) & (filtered_data['Year'] <= 2022)]
    
    # Pivot the data to get countries as rows and years as columns
    pivoted_data = filtered_data.pivot(index='Entity', columns='Year', values='Observation value - Indicator: Under-five mortality rate - Sex: Total - Wealth quintile: Total - Unit of measure: Deaths per 100 live births')

    # Ensure that the column names are integers (years)
    pivoted_data.columns = pivoted_data.columns.astype(int)
    
    return pivoted_data

if __name__ == "__main__":
    # Define the path to the raw CSV file
    file_path = '../../data/raw/healthData.csv'
    
    # Example: Filter by Algeria and Morocco (can be changed as needed)
    countries = []  # Can be set to None to include all countries
    
    # Call the function to clean and pivot the data with the given countries filter
    clean_data = clean_health_data(file_path, countries=countries)
    
    # Save the cleaned data to a new CSV file
    clean_data.to_csv('../../data/processed/clean_health_data.csv')  # Save cleaned data
