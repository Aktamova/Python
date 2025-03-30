Homework 1:

import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

In this task, use `.set_index` method to make Category column as index. 
Try this code, learn it and use it in the task.
> expenses.set_index('Category')

import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
1. Rename column names using function. "First Name" --> "first_name", "Age" --> "age
renamed_columns = {
    "First Name" : "first_name",
    "Age" : "age"
}

df.rename(columns=renamed_columns)
2. Print the first 3 rows of the DataFrame
df.head(3)
3. Find the mean age of the individuals
age_mean = df.Age.mean()
print(f"The mean is {age_mean}")
4. Select and print only the 'Name' and 'City' columns
df[['First Name', 'City']]
5. Add a new column 'Salary' with random salary values
import numpy as np  # For generating random salary values

# 1. Adding a 'Salary' column with random values between 50,000 and 100,000
np.random.seed(42)  # Ensures reproducibility
df['Salary'] = np.random.randint(50000, 100000, size=len(df))
6. Display summary statistics of the DataFrame
# 2. Displaying summary statistics
print(df)
print("\nSummary Statistics:\n", df.describe())

Homework 2:

1. Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data.
Use below table.

| Month | Sales | Expenses |
|-------|-------|----------|
| Jan   | 5000  | 3000     |
| Feb   | 6000  | 3500     |
| Mar   | 7500  | 4000     |
| Apr   | 8000  | 4500     |
import pandas as pd

data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
        'Sales': [5000, 6000, 7500, 8000],
        'Expenses': [3000, 3500, 4000, 4500]}
df = pd.DataFrame(data)
df
2. Calculate and display the maximum sales and expenses.
Sale_max = df.Sales.max()
Exp_max = df.Expenses.max()
print(f"The max sale is {Sale_max} \nThe max expenses is {Exp_max}")
3. Calculate and display the minimum sales and expenses.
Sale_min = df.Sales.min()
Exp_min = df.Expenses.min()
print(f"The min sale is {Sale_min} \nThe min expenses is {Exp_min}")
4. Calculate and display the average sales and expenses.
Sale_avg = df.Sales.mean()
Exp_avg = df.Expenses.mean()
print(f"The average sale is {Sale_avg} \nThe average expenses is {Exp_avg}")
Homework 3:

1. Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.

| Category       | January | February | March | April |
|----------------|---------|----------|-------|-------|
| Rent           | 1200    | 1300     | 1400  | 1500  |
| Utilities      | 200     | 220      | 240   | 250   |
| Groceries      | 300     | 320      | 330   | 350   |
| Entertainment  | 150     | 160      | 170   | 180   |
import pandas as pd

data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

df = pd.DataFrame(data)
df

2. Calculate and display the maximum expense for each category.
df.set_index('Category', inplace=True)
df['Max Expense'] = df[['January', 'February', 'March', 'April']].max(axis=1)
df

3. Calculate and display the minimum expense for each category.
df['Min Expense'] = df[['January', 'February', 'March', 'April']].min(axis=1)
df
4. Calculate and display the average expense for each category.
df['Avg Expense'] = df[['January', 'February', 'March', 'April']].mean(axis=1)
df[['Avg Expense']]
