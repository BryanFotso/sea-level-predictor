# Sea Level Predictor

This is the boilerplate for the Sea Level Predictor project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/sea-level-predictor

This project uses historical sea level data to predict future sea level changes. It visualizes the data through a scatter plot and fits two lines of best fit to predict sea level rise by 2050.

## Project Overview

The dataset contains historical sea level data from 1880 to the present. The objective is to predict future sea level changes based on historical trends, using two different methods of linear regression:

1. **Line of best fit for all available data**: The first regression line fits the data from the beginning (1880) up to the most recent data point.
2. **Line of best fit from the year 2000**: The second regression line only uses data from the year 2000 to the present to predict future sea level rise.

## Steps

- Import the sea level data from the `epa-sea-level.csv` file.
- Plot the data using a scatter plot.
- Apply linear regression using `scipy.stats.linregress` to compute the slope and y-intercept of the regression lines.
- Extend both regression lines to the year 2050 to predict future sea level changes.
- Display the scatter plot with both regression lines.
