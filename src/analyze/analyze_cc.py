import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.transform.transformations import load_raw_data, filter_countries, filter_years
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

def plot_country_data(country_data, country_name, years):
    plt.plot(years, country_data[years].iloc[0, :], label=country_name)

def plot_combined_data(morocco_data, algeria_data, years):
    plt.figure(figsize=(10, 6))
    plt.title("Comparison of Algeria and Morocco: Climate Change Indicators (1961-2022)")
    plt.xlabel("Year")
    plt.ylabel("Indicator Value")
    plot_country_data(morocco_data, 'Morocco', years)
    plot_country_data(algeria_data, 'Algeria', years)
    plt.legend()
    plt.grid(True)
    plt.xticks(years)
    plt.show()

def plot_scatter_plot(morocco_data, algeria_data, years):
    plt.figure(figsize=(10, 6))
    plt.title("Scatter Plot: Climate Change Indicators in Morocco vs. Algeria")
    plt.xlabel("Morocco Climate Change Indicators")
    plt.ylabel("Algeria Climate Change Indicators")
    morocco_values = morocco_data[years].iloc[0, :].values
    algeria_values = algeria_data[years].iloc[0, :].values
    plt.scatter(morocco_values, algeria_values, color='purple')
    plt.grid(True)
    plt.show()

def plot_heat_map(morocco_data, algeria_data, years):
    combined_data = pd.DataFrame({
        'Morocco': morocco_data[years].iloc[0, :].values,
        'Algeria': algeria_data[years].iloc[0, :].values,
    }, index=years)
    plt.figure(figsize=(10, 6))
    sns.heatmap(combined_data.T, cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5)
    plt.title("Heatmap: Climate Change Indicators for Morocco and Algeria")
    plt.xlabel("Years")
    plt.ylabel("Country")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    # Load raw data
    raw_data = load_raw_data('climate_change_indicators.csv')
    
    # Clean column names (strip spaces and standardize case)
    raw_data.columns = raw_data.columns.str.strip().str.title()
    
    # Filter data for specified countries
    filtered_data = filter_countries(raw_data, ['Algeria', 'Morocco'])
    
    # Filter for the required columns (Year columns only)
    filtered_data = filter_years(filtered_data)
    
    # Split the data by country
    morocco_data = filtered_data[filtered_data['Country'] == 'Morocco']
    algeria_data = filtered_data[filtered_data['Country'] == 'Algeria']
    
    # Define the years to display (every 5 years)
    years = [f'F{i}' for i in range(1961, 2023, 5)]  # This will give ['F1961', 'F1966', ..., 'F2021']
    
    # Plot combined data for both countries
    plot_combined_data(morocco_data, algeria_data, years)
    
    # Plot the scatter plot for both countries
    plot_scatter_plot(morocco_data, algeria_data, years)
    
    # Plot the heat map for both countries
    plot_heat_map(morocco_data, algeria_data, years)
