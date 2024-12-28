import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from statsmodels.tsa.arima.model import ARIMA
import os

# Load the processed data
def load_processed_data():
    processed_data_path = os.path.join('data', 'processed', 'climate_change_indicators_cleaned_Morocco_Algeria.csv')
    return pd.read_csv(processed_data_path)

# Function for linear regression modeling
# Function for linear regression modeling
def linear_regression(morocco_data, years):
    # Adjust X to match the years with available data
    X = np.array([i for i in range(1961, 2023, 5)]).reshape(-1, 1)  # Every 5 years as features
    y = morocco_data[years].iloc[0, :].values  # Indicator values as target

    model = LinearRegression()
    model.fit(X, y)

    future_years = np.array([i for i in range(2023, 2031)]).reshape(-1, 1)
    predictions = model.predict(future_years)

    # Plot the predictions
    plt.plot(future_years, predictions, label="Prediction", color='r')
    plt.legend()
    plt.show()


# Function for ARIMA time series forecasting
def arima_forecasting(morocco_data, years):
    y = morocco_data[years].iloc[0, :].values  # Indicator values

    model = ARIMA(y, order=(5, 1, 0))  # (p, d, q) parameters
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=10)

    # Plot forecast
    plt.plot(range(1961, 2023), y, label="Historical Data")
    plt.plot(range(2023, 2031), forecast, label="Forecast", color='r')
    plt.legend()
    plt.show()

# Function for Random Forest Modeling
def random_forest_regression(morocco_data, years):
    X = np.array([i for i in range(1961, 2023)]).reshape(-1, 1)
    y = morocco_data[years].iloc[0, :].values

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)

    future_years = np.array([i for i in range(2023, 2031)]).reshape(-1, 1)
    predictions = model.predict(future_years)

    # Plot predictions
    plt.plot(future_years, predictions, label="Prediction", color='g')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Load processed data (already cleaned and filtered)
    processed_data = load_processed_data()

    # Extract data for Morocco and the years
    morocco_data = processed_data[processed_data['Country'] == 'Morocco']
    years = [f'F{i}' for i in range(1961, 2023, 5)]  # Every 5 years

    # Call the model functions
    linear_regression(morocco_data, years)
    arima_forecasting(morocco_data, years)
    random_forest_regression(morocco_data, years)
