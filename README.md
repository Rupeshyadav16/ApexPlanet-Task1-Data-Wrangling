# Data Dictionary

| Column Name   | Description                                                |
| ------------- | ---------------------------------------------------------- |
| Order_ID      | Unique order identifier                                    |
| Order_Date    | Date of order                                              |
| Customer_ID   | Unique customer identifier                                 |
| Customer_Name | Customer name                                              |
| Age           | Customer age                                               |
| Gender        | Customer gender                                            |
| City          | Customer city                                              |
| Product       | Purchased product                                          |
| Category      | Product category                                           |
| Quantity      | Quantity purchased                                         |
| Unit_Price    | Price per unit                                             |
| Total_Sales   | Total sales amount                                         |
| Age_Group     | Customer age category (created during feature engineering) |
| Order_Month   | Month extracted from order date                            |


# ApexPlanet Internship - Task 1

## Project Title

Data Immersion & Wrangling

## Objective

To analyze, clean, and prepare the provided dataset for further business analysis.

## Tools Used

* Python
* Pandas
* OpenPyXL
* VS Code

## Data Quality Issues Found

* 20 missing values in Age column
* 13 missing values in City column
* No duplicate rows found

## Cleaning Steps Performed

1. Loaded dataset
2. Checked missing values
3. Filled missing Age values using median
4. Filled missing City values using mode
5. Converted Order_Date into datetime format
6. Removed duplicate records
7. Created Age_Group feature
8. Created Order_Month feature

## Output

Cleaned_Sales_Dataset.xlsx

## Author

Rupesh Kumar
