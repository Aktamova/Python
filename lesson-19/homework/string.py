import pandas as pd

sales_data = pd.read_csv('sales_data.csv')

category_stats = sales_data.groupby('Category').agg(
    total_quantity_sold=('Quantity', 'sum'),
    average_price_per_unit=('Price', 'mean'),
    max_quantity_single_transaction=('Quantity', 'max')
)

print("Category Statistics:")
print(category_stats)

# Identify the top-selling product in each category
top_selling_product = sales_data.groupby('Category').apply(
    lambda x: x.groupby('Product')['Quantity'].sum().idxmax()
).reset_index(name='Top_Selling_Product')

print("\nTop-Selling Products by Category:")
print(top_selling_product)

# Calculate total sales and find the date with the highest sales
sales_data['total_sales'] = sales_data['Quantity'] * sales_data['Price']
highest_sales_date = sales_data.groupby('Date')['total_sales'].sum().idxmax()

print("\nDate with Highest Total Sales:")
print(highest_sales_date)

import pandas as pd

customer_orders = pd.read_csv('customer_orders.csv')

# Task 1: Group data by CustomerID and filter out customers with less than 20 orders
customer_order_counts = customer_orders.groupby('CustomerID').size()
customers_with_20_or_more_orders = customer_order_counts[customer_order_counts >= 20].index
filtered_orders_by_customer = customer_orders[customer_orders['CustomerID'].isin(customers_with_20_or_more_orders)]

print("Customers with 20 or more orders:")
print(filtered_orders_by_customer)

# Task 2: Identify customers who have ordered products with an average price per unit greater than $120
average_price_per_customer = customer_orders.groupby('CustomerID').apply(
    lambda x: (x['Price'].mean()) > 120
)
customers_with_high_avg_price = average_price_per_customer[average_price_per_customer].index
filtered_orders_by_high_avg_price = customer_orders[customer_orders['CustomerID'].isin(customers_with_high_avg_price)]

print("\nCustomers with average price per unit greater than $120:")
print(filtered_orders_by_high_avg_price)

# Task 3: Find total quantity and total price for each product and filter out products with a total quantity less than 5
product_stats = customer_orders.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', 'sum')
)
filtered_product_stats = product_stats[product_stats['total_quantity'] >= 5]

print("\nProducts with total quantity greater than or equal to 5 units:")
print(filtered_product_stats)

import sqlite3
import pandas as pd

# Load the salary categories from the Excel file
salary_bands = pd.read_excel('population_salary_analysis.xlsx')

# Connect to the SQLite database
conn = sqlite3.connect('population.db')

# Read the population data from the database
query = "SELECT * FROM population"
population_data = pd.read_sql(query, conn)

# Close the database connection
conn.close()

# Merge the population data with the salary bands
population_data = population_data.merge(salary_bands, on='SalaryBand', how='left')

# Task 1: Calculate the percentage of population for each salary category
salary_category_counts = population_data['SalaryBand'].value_counts()
total_population = len(population_data)
percentage_population = (salary_category_counts / total_population) * 100

# Task 2: Calculate the average salary in each salary category
average_salary = population_data.groupby('SalaryBand')['Salary'].mean()

# Task 3: Calculate the median salary in each salary category
median_salary = population_data.groupby('SalaryBand')['Salary'].median()

# Task 4: Calculate the number of people in each salary category
population_count = salary_category_counts

# Display the results
print("Percentage of population in each salary category:")
print(percentage_population)

print("\nAverage salary in each salary category:")
print(average_salary)

print("\nMedian salary in each salary category:")
print(median_salary)

print("\nNumber of people in each salary category:")
print(population_count)

# Task 5: Calculate the same measures per State
state_salary_category_counts = population_data.groupby('State')['SalaryBand'].value_counts()
state_percentage_population = state_salary_category_counts / state_salary_category_counts.groupby('State').sum() * 100

state_average_salary = population_data.groupby(['State', 'SalaryBand'])['Salary'].mean()
state_median_salary = population_data.groupby(['State', 'SalaryBand'])['Salary'].median()
state_population_count = state_salary_category_counts

# Display the results per State
print("\nPercentage of population in each salary category per State:")
print(state_percentage_population)

print("\nAverage salary in each salary category per State:")
print(state_average_salary)

print("\nMedian salary in each salary category per State:")
print(state_median_salary)

print("\nNumber of people in each salary category per State:")
print(state_population_count)
