

# Stress-Strain Analyzer

### A Python based tool that analyzes force-extension data. 

# Features:
- Generates a stress-strain curve using CSV file data.
- Calculates the elastic region of the material.
- Computes Young's Modulus.
- Computes yield strength (0.2% offset).
- Accounts for random noise in data using linear regression. 

# Background:
I made this project as a first-year mechanical engineering student to expand my portfolio and get a head-start on second-year materials topics. I learned about calculating stress and strain, Young's Modulus, yield strength, as well as improving my Python skills of course.

# How it was Made:

## Stress-Strain Calculation:

- Force-extenstion data is given in CSV file format.
- User input is taken to find initial length(mm) and cross-sectional area (mm^2).
- Stress and strain arrays are generated using this data.

## Elastic Region Calculation:

- Linear regression is used after the fifth stress-strain data point (first 5 are assumed to be linear).
- An R^2 value of 0.995 is used.
- All data points before an R^2 < 0.995 are considered elastic.
- Array of all elastic stress-strain points is stored.

## Plotting:

- Plot of all stress-strain points is plotted.
- Overlayed on the plot is a plot of the elastic points in a different colour.
- Plotting done in matplotlib.

# Imports:
matplotlib.pylpot
- For graphing data and labelling important regions.

numpy:
- For data manipulation and analysis.

