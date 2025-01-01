import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def filter_countries(data, countries):
    return data[data['Entity'].isin(countries)]

def filter_years(data, start_year, end_year):
    return data[(data['Year'] >= start_year) & (data['Year'] <= end_year)]

def pivot_data(data):
    return data.pivot(index='Entity', columns='Year', values='emissions_total')

def plot_country_data(country_data, country_name, years):
    # Use .loc to select the relevant years for plotting
    country_data_for_years = country_data.loc[years].values
    plt.plot(years, country_data_for_years, label=country_name)

def plot_combined_data(morocco_data, algeria_data, years):
    plt.figure(figsize=(10, 6))
    plt.title("Comparison of Algeria and Morocco: CO2 Emissions (1970-2020)")
    plt.xlabel("Year")
    plt.ylabel("CO2 Emissions (Million Tonnes)")
    plot_country_data(morocco_data, 'Morocco', years)
    plot_country_data(algeria_data, 'Algeria', years)
    plt.legend()
    plt.grid(True)
    plt.xticks(years)
    plt.show()

def plot_scatter_plot(morocco_data, algeria_data, years):
    plt.figure(figsize=(10, 6))
    plt.title("Scatter Plot: CO2 Emissions in Morocco vs. Algeria")
    plt.xlabel("Morocco CO2 Emissions")
    plt.ylabel("Algeria CO2 Emissions")
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
    plt.title("Heatmap: CO2 Emissions for Morocco and Algeria")
    plt.xlabel("Years")
    plt.ylabel("Country")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    raw_data = pd.read_csv('C:/Users/SWIFT 3/pythonEtlProject/data/raw/co2_emissions.csv')
    raw_data.columns = raw_data.columns.str.strip()

    filtered_data = filter_countries(raw_data, ['Morocco', 'Algeria'])
    filtered_data = filter_years(filtered_data, 1970, 2020)

    pivoted_data = pivot_data(filtered_data)

    # Ensure that the column names are integers (years)
    pivoted_data.columns = pivoted_data.columns.astype(int)

    morocco_data = pivoted_data.loc['Morocco']
    algeria_data = pivoted_data.loc['Algeria']

    # Define years from 1970 to 2022 with a step of 5 years
    years = list(range(1970, 2020, 5))

    plot_combined_data(morocco_data, algeria_data, years)
    plot_scatter_plot(morocco_data, algeria_data, years)
    plot_heat_map(morocco_data, algeria_data, years)
