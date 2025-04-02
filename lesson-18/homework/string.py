import pandas as pd
df = pd.read_csv('tackoverflow_qa.csv')
df.head()
Find all questions that were created before 2014
df['creationdate'] = pd.to_datetime(df['creationdate'], errors='coerce')
df = df.dropna(subset=['creationdate'])

filtered_df = df[df['creationdate'].dt.year < 2014]
print(filtered_df)
Find all questions with a score more than 50
df['score'] = pd.to_numeric(df['score'], errors='coerce')

high_score_df = df[df['score'] > 50]
print(high_score_df)
Find all questions with a score between 50 and 100
df['score'] = pd.to_numeric(df['score'], errors='coerce')

filtered_df = df[(df['score'] > 50) & (df['score'] < 100)]
print(filtered_df)
Find all questions answered by Scott Boston
filtered_df = df[df['ans_name'] == 'Scott Boston']
print(filtered_df)
Find all questions answered by the following 5 users
Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
df['creationdate'] = pd.to_datetime(df['creationdate'], errors='coerce')
df['score'] = pd.to_numeric(df['score'], errors='coerce')

start_date = "2014-03-01"
end_date = "2014-10-31"

# Filter questions based on conditions
filtered_df = df[
    (df['creationdate'] >= start_date) & 
    (df['creationdate'] <= end_date) & 
    (df['ans_name'] == 'Unutbu') & 
    (df['score'] < 5)
]

print(filtered_df)
Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
df['score'] = pd.to_numeric(df['score'], errors='coerce')
df['viewcount'] = pd.to_numeric(df['viewcount'], errors='coerce')

filtered_df = df[(df['score'].between(5, 10)) | (df['viewcount'] > 10000)]
print(filtered_df)
Find all questions that are not answered by Scott Boston
filtered_df = df[df['ans_name'] != 'Scott Boston']
print(filtered_df)
titanic_df = pd.read_csv("titanic.csv")
titanic_df.head()
Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
titanic_df['Age'] = pd.to_numeric(titanic_df['Age'], errors='coerce')

filtered_df = titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Pclass'] == 1) & (titanic_df['Age'].between(20, 30))]
print(filtered_df)
Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
filtered_df = titanic_df[titanic_df['Fare'] > 100]
print(filtered_df)
Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
filtered_df = titanic_df[(titanic_df['Survived'] == 1) & 
                          (titanic_df['SibSp'] == 0) & 
                          (titanic_df['Parch'] == 0)]

print(filtered_df)

Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
filtered_df = titanic_df[(titanic_df['Embarked'] == 'C') & 
                          (titanic_df['Fare'] > 50)]
print(filtered_df)

Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
filtered_df = titanic_df[(titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)]
print(filtered_df)

Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.
filtered_df = titanic_df[(titanic_df['Age'] <= 15) & (titanic_df['Survived'] == 0)]

print(filtered_df)

Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
filtered_df = titanic_df[(titanic_df['Cabin'].notna()) & (titanic_df['Fare'] > 200)]

print(filtered_df)

Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.
filtered_df = titanic_df[titanic_df['PassengerId'] % 2 != 0]

print(filtered_df)

Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.
filtered_df = titanic_df[titanic_df['Ticket'].duplicated(keep=False) == False]
print(filtered_df)
Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
filtered_df = titanic_df[(titanic_df['Sex'] == 'female') & 
                          (titanic_df['Name'].str.contains('Miss', case=False)) & 
                          (titanic_df['Pclass'] == 1)]

print(filtered_df)
