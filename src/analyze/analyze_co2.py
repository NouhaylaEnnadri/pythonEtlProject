import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.extract.download_CO2_data import load_raw_data, filter_countries, filter_years
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

def plot_country_data(country_data, country_name, years):
    # Plot emissions for a given country over the years
    plt.plot(years, country_data[years].iloc[0, :], label=country_name)

def plot_combined_data(morocco_data, algeria_data, years):
    # Combined line plot of emissions for both Morocco and Algeria
    plt.figure(figsize=(10, 6))
    plt.title("CO2 Emissions Comparison: Morocco vs Algeria (1960-2022)")
    plt.xlabel("Year")
    plt.ylabel("CO2 Emissions (Million Tonnes)")
    plot_country_data(morocco_data, 'Morocco', years)
    plot_country_data(algeria_data, 'Algeria', years)
    plt.legend()
    plt.grid(True)
    plt.xticks(years)
    plt.show()

def plot_scatter_plot(morocco_data, algeria_data, years):
    # Scatter plot to compare CO2 emissions between Morocco and Algeria
    plt.figure(figsize=(10, 6))
    plt.title("Scatter Plot: CO2 Emissions in Morocco vs Algeria")
    plt.xlabel("Morocco CO2 Emissions (Million Tonnes)")
    plt.ylabel("Algeria CO2 Emissions (Million Tonnes)")
    morocco_values = morocco_data[years].iloc[0, :].values
    algeria_values = algeria_data[years].iloc[0, :].values
    plt.scatter(morocco_values, algeria_values, color='purple')
    plt.grid(True)
    plt.show()

def plot_heat_map(morocco_data, algeria_data, years):
    # Create a heatmap to compare CO2 emissions for both countries over the years
    combined_data = pd.DataFrame({
        'Morocco': morocco_data[years].iloc[0, :].values,
        'Algeria': algeria_data[years].iloc[0, :].values,
    }, index=years)
    plt.figure(figsize=(10, 6))
    sns.heatmap(combined_data.T, cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5)
    plt.title("Heatmap: CO2 Emissions for Morocco and Algeria")
    plt.xlabel("Years")
    plt.ylabel("Country")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    # Load raw data
    raw_data = load_raw_data('co2_emissions.csv')
    
    # Clean column names (strip spaces and standardize case)
    raw_data.columns = raw_data.columns.str.strip().str.title()
    
    # Filter data for Morocco and Algeria
    filtered_data = filter_countries(raw_data, ['Morocco', 'Algeria'])
    
    # Filter for years from 1960 to 2022
    filtered_data = filter_years(filtered_data, start_year=1960, end_year=2022)
    
    # Split the data by country
    morocco_data = filtered_data[filtered_data['Entity'] == 'Morocco']
    algeria_data = filtered_data[filtered_data['Entity'] == 'Algeria']
    
    # Define the years to display (1960 to 2022)
    years = [str(year) for year in range(1960, 2023)]  # This will give ['1960', '1961', ..., '2022']
    
    # Plot combined data for both countries
    plot_combined_data(morocco_data, algeria_data, years)
    
    # Plot the scatter plot for both countries
    plot_scatter_plot(morocco_data, algeria_data, years)
    
    # Plot the heat map for both countries
    plot_heat_map(morocco_data, algeria_data, years)
