import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Generate years from 1880 to 2050 for prediction
    years_full_range = np.arange(1880, 2051, 1)
    
    # Predict sea level using the regression formula (y = slope * x + intercept) for all years 1880-2050
    predicted_values_full_range = slope * years_full_range + intercept
    plt.plot(years_full_range, predicted_values_full_range, label='Fit line (1880-present)')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Generate years from 2000 to 2050 for prediction
    years_recent_range = np.arange(2000, 2051, 1)
    
    # Predict sea level using the regression formula (y = slope * x + intercept) for years 2000-2050
    predicted_values_recent = slope_recent * years_recent_range + intercept_recent
    plt.plot(years_recent_range, predicted_values_recent, label='Fit line (2000-present)', color='red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Set x-ticks to match the expected range and interval
    x_ticks = np.arange(1850, 2080, 25)  # Adjusted range to include 2075
    plt.xticks(x_ticks)    # Ensure float type x-tick labels

    # Add legend
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
