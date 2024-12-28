import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from src.transform.transformations_temp import load_raw_data, filter_countries, remove_columns, filter_years

def plot_country_data(country_data, country_name, years):
    plt.plot(years, country_data[years].iloc[0, :], label=country_name)

def plot_combined_data(morocco_data, algeria_data, years):
    plt.figure(figsize=(10, 6))
    plt.title("Comparison of Algeria and Morocco: Temperature Indicators (1961-2022)")
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
    plt.title("Scatter Plot: Temperature Indicators in Morocco vs. Algeria")
    plt.xlabel("Morocco Temperature Indicators")
    plt.ylabel("Algeria Temperature Indicators")
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
    plt.title("Heatmap: Temperature Indicators for Morocco and Algeria")
    plt.xlabel("Years")
    plt.ylabel("Country")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    raw_data = load_raw_data('temperature_data.csv')
    raw_data.columns = raw_data.columns.str.strip().str.title()
    filtered_data = filter_countries(raw_data, ['Algeria', 'Morocco'])
    filtered_data = remove_columns(filtered_data, ['Unit'])
    filtered_data = filter_years(filtered_data)
    
    morocco_data = filtered_data[filtered_data['Country Name'] == 'Morocco']
    algeria_data = filtered_data[filtered_data['Country Name'] == 'Algeria']
    years = [col for col in morocco_data.columns if col.isdigit()]

    # Plot combined data
    plot_combined_data(morocco_data, algeria_data, years)

    # Plot scatter plot
    plot_scatter_plot(morocco_data, algeria_data, years)

    # Plot heat map
    plot_heat_map(morocco_data, algeria_data, years)
