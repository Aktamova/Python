import pandas as pd
import matplotlib.pyplot as plt

# Data provided
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

# Create the DataFrame
df1 = pd.DataFrame(data1)

# Exercise 1: Calculate the average grade for each student
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)

# Exercise 2: Find the student with the highest average grade
top_student = df1.loc[df1['Average'].idxmax()]

# Exercise 3: Create a new column 'Total' representing the total marks obtained by each student
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)

# Exercise 4: Plot a bar chart to visualize the average grades in each subject
subject_averages = df1[['Math', 'English', 'Science']].mean()

# Plot the bar chart
subject_averages.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Average Grades in Each Subject')
plt.xlabel('Subjects')
plt.ylabel('Average Grade')
plt.xticks(rotation=0)
plt.show()

# Display results
print("Exercise 1: Average grade for each student:")
print(df1[['Student_ID', 'Average']])

print("\nExercise 2: Student with the highest average grade:")
print(top_student[['Student_ID', 'Average']])

print("\nExercise 3: Data with Total marks for each student:")
print(df1[['Student_ID', 'Total']])



# Data provided
data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

# Create the DataFrame
df2 = pd.DataFrame(data2)

# Exercise 1: Calculate the total sales for each product
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()

# Exercise 2: Find the date with the highest total sales
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
highest_sales_date = df2.loc[df2['Total_Sales'].idxmax()]

# Exercise 3: Calculate the percentage change in sales for each product from the previous day
percentage_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100

# Exercise 4: Plot a line chart to visualize the sales trends for each product over time
df2.set_index('Date')[['Product_A', 'Product_B', 'Product_C']].plot(kind='line', figsize=(10, 6))
plt.title('Sales Trends for Each Product')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.legend(title='Products')
plt.tight_layout()
plt.show()

# Display results
print("Exercise 1: Total sales for each product:")
print(total_sales)

print("\nExercise 2: Date with the highest total sales:")
print(highest_sales_date[['Date', 'Total_Sales']])

print("\nExercise 3: Percentage change in sales for each product from the previous day:")
print(percentage_change)

import pandas as pd
import matplotlib.pyplot as plt

# Data provided
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

# Create the DataFrame
df3 = pd.DataFrame(data3)

# Exercise 1: Calculate the average salary for each department
avg_salary_by_department = df3.groupby('Department')['Salary'].mean()

# Exercise 2: Find the employee with the most experience
most_experienced_employee = df3.loc[df3['Experience (Years)'].idxmax()]

# Exercise 3: Create a new column 'Salary Increase' representing the percentage increase in salary from the minimum salary in the dataframe
min_salary = df3['Salary'].min()
df3['Salary Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100

# Exercise 4: Plot a bar chart to visualize the distribution of employees across different departments
department_counts = df3['Department'].value_counts()

# Plot the bar chart
department_counts.plot(kind='bar', color='skyblue', figsize=(8, 6))
plt.title('Distribution of Employees Across Different Departments')
plt.xlabel('Departments')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Display results
print("Exercise 1: Average salary for each department:")
print(avg_salary_by_department)

print("\nExercise 2: Employee with the most experience:")
print(most_experienced_employee[['Employee_ID', 'Name', 'Experience (Years)']])

print("\nExercise 3: Data with Salary Increase percentages:")
print(df3[['Employee_ID', 'Name', 'Salary', 'Salary Increase']])

import pandas as pd
import matplotlib.pyplot as plt

# Data provided
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

# Create the DataFrame
df4 = pd.DataFrame(data4)

# Exercise 1: Calculate the total revenue from all orders
total_revenue = df4['Total_Price'].sum()

# Exercise 2: Find the most ordered product
most_ordered_product = df4['Product'].mode()[0]

# Exercise 3: Calculate the average quantity of products ordered
average_quantity = df4['Quantity'].mean()

# Exercise 4: Plot a pie chart to visualize the distribution of sales across different products
product_sales = df4.groupby('Product')['Total_Price'].sum()

# Plot the pie chart
product_sales.plot(kind='pie', autopct='%1.1f%%', figsize=(7, 7), colors=['skyblue', 'lightgreen', 'lightcoral'])
plt.title('Sales Distribution Across Different Products')
plt.ylabel('')  # Hides the ylabel
plt.show()

# Display results
print(f"Exercise 1: Total revenue from all orders: ${total_revenue}")
print(f"Exercise 2: Most ordered product: {most_ordered_product}")
print(f"Exercise 3: Average quantity of products ordered: {average_quantity}")
