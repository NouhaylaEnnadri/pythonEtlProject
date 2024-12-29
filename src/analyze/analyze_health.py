import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_country_data(country_data, country_name, years):
    print(f"Available years in {country_name}: {country_data.index}")  # Debugging line to check available years
    # Ensure the years are in the correct format for selection
    country_data_for_years = country_data.loc[years].values
    plt.plot(years, country_data_for_years, label=country_name)

def plot_combined_data(morocco_data, algeria_data, years):
    plt.figure(figsize=(10, 6))
    plt.title("Comparison of Algeria and Morocco: Under-five Mortality Rate (1960-2022)")
    plt.xlabel("Year")
    plt.ylabel("Under-five Mortality Rate (Deaths per 100 live births)")
    plot_country_data(morocco_data, 'Morocco', years)
    plot_country_data(algeria_data, 'Algeria', years)
    plt.legend()
    plt.grid(True)
    plt.xticks(years)
    plt.show()

def plot_scatter_plot(morocco_data, algeria_data, years):
    plt.figure(figsize=(10, 6))
    plt.title("Scatter Plot: Under-five Mortality Rate in Morocco vs. Algeria")
    plt.xlabel("Morocco Mortality Rate")
    plt.ylabel("Algeria Mortality Rate")
    morocco_values = morocco_data.loc[years].values
    algeria_values = algeria_data.loc[years].values
    plt.scatter(morocco_values, algeria_values, color='purple')
    plt.grid(True)
    plt.show()

def plot_heat_map(morocco_data, algeria_data, years):
    combined_data = pd.DataFrame({
        'Morocco': morocco_data.loc[years].values,
        'Algeria': algeria_data.loc[years].values,
    }, index=years)
    plt.figure(figsize=(10, 6))
    sns.heatmap(combined_data.T, cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5)
    plt.title("Heatmap: Under-five Mortality Rate for Morocco and Algeria")
    plt.xlabel("Years")
    plt.ylabel("Country")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    # Load the cleaned data
    clean_health_data = pd.read_csv('C:/Users/SWIFT 3/pythonEtlProject/data/processed/clean_health_data.csv', index_col=0)
    
    # Define years from 1960 to 2022 with a step of 5 years
    years = [str(year) for year in range(1960, 2023, 5)]
    
    # Extract data for Morocco and Algeria as Series
    morocco_data = clean_health_data.loc['Morocco']
    algeria_data = clean_health_data.loc['Algeria']
    
    # Check if the years are available in the data
    print(f"Years in Morocco data: {morocco_data.index}")
    print(f"Years in Algeria data: {algeria_data.index}")
    
    # Plot the data
    plot_combined_data(morocco_data, algeria_data, years)
    plot_scatter_plot(morocco_data, algeria_data, years)
    plot_heat_map(morocco_data, algeria_data, years)
