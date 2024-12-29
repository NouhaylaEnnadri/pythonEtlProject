# transformations_health.py
import pandas as pd

def clean_health_data(file_path):
    # Load the dataset
    health_data = pd.read_csv(file_path)
    
    # Remove extra spaces from column names
    health_data.columns = health_data.columns.str.strip()
    
    # Filter for Morocco and Algeria
    filtered_data = health_data[health_data['Entity'].isin(['Morocco', 'Algeria'])]
    
    # Filter for years between 1960 and 2022
    filtered_data = filtered_data[(filtered_data['Year'] >= 1970) & (filtered_data['Year'] <= 2020)]
    
    # Pivot the data to get countries as rows and years as columns
    pivoted_data = filtered_data.pivot(index='Entity', columns='Year', values='Observation value - Indicator: Under-five mortality rate - Sex: Total - Wealth quintile: Total - Unit of measure: Deaths per 100 live births')

    # Ensure that the column names are integers (years)
    pivoted_data.columns = pivoted_data.columns.astype(int)
    
    return pivoted_data

if __name__ == "__main__":
    file_path = 'C:/Users/SWIFT 3/pythonEtlProject/data/raw/healthData.csv'
    clean_data = clean_health_data(file_path)
    clean_data.to_csv('C:/Users/SWIFT 3/pythonEtlProject/data/processed/clean_health_data.csv')  # Save cleaned data
