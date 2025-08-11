**Python Pandas Project: Data Cleaning**

This project demonstrates a simple Python script using Pandas to clean input CSV data.

The script performs the following steps:

1\. Loads the input CSV file

2\. Checks for missing values and handles them:

&nbsp;  - Drops completely empty rows

&nbsp;  - Fills missing categorical values (Region, Category) with default values

&nbsp;  - Fills missing numeric values (Age) with the column mean

3\. Calculates a new column: Total = Quantity \* UnitPrice

4\. Sorts the data by the 'Total' column (descending)

5\. Outputs a cleaned CSV file ready for further analysis
