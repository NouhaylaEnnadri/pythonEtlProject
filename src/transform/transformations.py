import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to the raw data folder
RAW_DATA_PATH = os.path.join('data', 'raw')
PROCESSED_DATA_PATH = os.path.join('data', 'processed')

# Load the data (already filtered for Algeria and Morocco)
def load_raw_data(file_name):
    file_path = os.path.join(RAW_DATA_PATH, file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_name} not found in {RAW_DATA_PATH}")
    return pd.read_csv(file_path)

def filter_countries(data, countries):
    # Filter rows for the specified countries (e.g., Algeria and Morocco)
    filtered_data = data[data['Country'].isin(countries)]
    return filtered_data

def filter_years(data):
    # Extract columns for years from F1961 to F2022
    year_columns = [f'F{i}' for i in range(1961, 2023)]
    data = data[['Country'] + year_columns]  # Include 'Country' and year columns
    return data

def plot_country_data(country_data, country_name, years):
    # Plot only the data for the years specified
    plt.plot(years, country_data[years].iloc[0, :], label=country_name)

def plot_combined_data(morocco_data, algeria_data, years):
    plt.figure(figsize=(10, 6))
    plt.title("Comparison of Algeria and Morocco: Climate Change Indicators (1961-2022)")
    plt.xlabel("Year")
    plt.ylabel("Indicator Value")
    
    # Plot Morocco
    plot_country_data(morocco_data, 'Morocco', years)
    
    # Plot Algeria
    plot_country_data(algeria_data, 'Algeria', years)
    
    # Show the graph with legend
    plt.legend()
    plt.grid(True)
    plt.xticks(years)  # Set x-ticks to the years every 5 years
    plt.show()

if __name__ == "__main__":
    # Load raw data
    raw_data = load_raw_data('climate_change_indicators.csv')
    
    # Clean up column names (strip spaces and standardize case)
    raw_data.columns = raw_data.columns.str.strip().str.title()
    
    # Filter for the specified countries (Algeria and Morocco)
    filtered_data = filter_countries(raw_data, ['Algeria', 'Morocco'])
    
    # Filter for the required columns (Year columns only)
    filtered_data = filter_years(filtered_data)
    
    # Split the data by country
    morocco_data = filtered_data[filtered_data['Country'] == 'Morocco']
    algeria_data = filtered_data[filtered_data['Country'] == 'Algeria']
    
    # Define the years to display (every 5 years)
    years = [f'F{i}' for i in range(1961, 2023, 5)]  # This will give ['F1961', 'F1966', ..., 'F2021']
    
    # Plot the individual data for each country (Morocco)
    plt.figure(figsize=(10, 6))
    plt.title("Climate Change Indicators in Morocco (1961-2022)")
    plt.xlabel("Year")
    plt.ylabel("Indicator Value")
    plt.plot(years, morocco_data[years].iloc[0, :], label="Morocco", color='b')
    plt.xticks(years)  # Set x-ticks to the years every 5 years
    plt.grid(True)
    plt.legend()
    plt.show()

    # Plot the individual data for each country (Algeria)
    plt.figure(figsize=(10, 6))
    plt.title("Climate Change Indicators in Algeria (1961-2022)")
    plt.xlabel("Year")
    plt.ylabel("Indicator Value")
    plt.plot(years, algeria_data[years].iloc[0, :], label="Algeria", color='g')
    plt.xticks(years)  # Set x-ticks to the years every 5 years
    plt.grid(True)
    plt.legend()
    plt.show()

    # Plot the combined data for both countries
    plot_combined_data(morocco_data, algeria_data, years)
