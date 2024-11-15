import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Scatter plot of the data
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    # Perform linear regression for the entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Plot the line of best fit
    years_extended = range(1880, 2051)  # From 1880 to 2050
    sea_level_line = [slope * year + intercept for year in years_extended]
    plt.plot(years_extended, sea_level_line, label='Best Fit Line (1880-2050)')

    # Create second line of best fit
    # Filter data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]

    # Perform linear regression on the filtered data
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    # Plot the second line of best fit
    # Define the years range from 2000 to 2050 for the second line of best fit
    years_recent_extended = range(2000, 2051)
    sea_level_line_recent = [slope_recent * year + intercept_recent for year in years_recent_extended]
    plt.plot(years_recent_extended, sea_level_line_recent, label='Best Fit Line (2000-2050)', color='red')

    # Add labels and title
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()