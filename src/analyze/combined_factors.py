import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_merge_data(health_file, temp_file):
    # Load health data
    health_data = pd.read_csv(health_file, index_col=0)

    # Load temperature data
    temp_data = pd.read_csv(temp_file)
    temp_data.columns = temp_data.columns.str.strip().str.title()

    # Filter Morocco and Algeria data from temperature
    temp_data = temp_data[temp_data['Country Name'].isin(['Morocco', 'Algeria'])]
    temp_data.set_index(['Country Name'], inplace=True)

    # Keep only numeric columns (years)
    temp_data = temp_data.loc[:, temp_data.columns.str.isdigit()]

    # Transpose temperature data for merging
    temp_data = temp_data.T
    temp_data.index.name = 'Year'

    # Merge health and temperature data on Year for Morocco and Algeria
    merged_data = health_data.T.merge(temp_data, left_index=True, right_index=True, suffixes=('_health', '_temp'))

    # Reset index for plotting
    merged_data.reset_index(inplace=True)

    return merged_data

def plot_combined_trends(merged_data, country):
    plt.figure(figsize=(12, 6))
    plt.title(f"Combined Trends: {country} (Health and Temperature)")
    plt.xlabel("Year")
    plt.ylabel("Value")

    # Extract data for the specified country
    country_data = merged_data[["Year", f"{country}_health", f"{country}_temp"]]

    # Plot health and temperature data
    plt.plot(country_data["Year"], country_data[f"{country}_health"], label="Health Indicator", marker='o')
    plt.plot(country_data["Year"], country_data[f"{country}_temp"], label="Temperature Indicator", marker='s')

    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()

def plot_correlation_heatmap(merged_data):
    plt.figure(figsize=(10, 6))
    sns.heatmap(merged_data.corr(), cmap="coolwarm", annot=True, fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap: Health and Temperature Indicators")
    plt.show()

def main():
    health_file = 'C:/Users/SWIFT 3/pythonEtlProject/data/processed/clean_health_data.csv'
    temp_file = 'C:/Users/SWIFT 3/pythonEtlProject/data/processed/temperature_data.csv'

    # Load and merge data
    merged_data = load_and_merge_data(health_file, temp_file)

    # Plot combined trends for Morocco
    plot_combined_trends(merged_data, 'Morocco')

    # Plot combined trends for Algeria
    plot_combined_trends(merged_data, 'Algeria')

    # Plot correlation heatmap
    plot_correlation_heatmap(merged_data)

if __name__ == "__main__":
    main()
