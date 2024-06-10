import pandas as pd

# Load the CSV file into a Pandas DataFrame
file_path = ('C:\\Users\\SWAPNA\\Downloads\\task2dataset_data.csv')
myfile = pd.read_csv(file_path)

# Display the DataFrame to understand its structure
print("Initial DataFrame:")
print(myfile)

# Filter data based on conditions (e.g., Age greater than 30)
filtered_myfile = myfile[myfile['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):")
print(filtered_myfile)

# Handle missing values by filling with mean of the column
myfile.isnull()
myfile['Age'].fillna(myfile['Age'].mean(), inplace=True)
myfile['Salary'].fillna(myfile['Salary'].mean(), inplace=True)
print("\nDataFrame after handling missing values:")
print(myfile)

# Calculate summary statistics for the 'Salary' column
salary_mean = myfile['Salary'].mean()
salary_median = myfile['Salary'].median()
salary_std = myfile['Salary'].std()

print("\nSummary Statistics for Salary:")
print(f"Mean: {salary_mean}")
print(f"Median: {salary_median}")
print(f"Standard Deviation: {salary_std}")