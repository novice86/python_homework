import pandas as pd
# Task1

# Create a DataFrame from dictionary
task1_dict = {
    "Name": ['Alice', 'Bob', 'Charlie'],
    "Age": [25, 30, 35],
    "City": ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(task1_dict)
print(task1_data_frame)
print(f"task1_data_frame: {task1_data_frame}")

# Add a new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary["Salary"] = pd.Series([70000, 80000, 90000])
print(f"task1_with_salary: {task1_with_salary}")

# Modify an existing column
task1_older = task1_with_salary.copy()
task1_older["Age"] = task1_older["Age"] + 1
print(f"task1_older: {task1_older}")

# Save the DataFrame as a CSV file
task1_older.to_csv("employees.csv", header=True, index=False)


# Task2

# Read data from a CSV file
task2_employees = pd.read_csv("employees.csv")
print(f"task2_employees: {task2_employees}")

# Read data from a JSON file
json_employees = pd.read_json("additional_employees.json")
print(f"json_employees: {json_employees}")

# Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees],ignore_index=True)
print(f"more_employees: {more_employees}")

# Task3

# Use the head() method
first_three = more_employees.head(3)
print(f"first_three: {first_three}")

# Use the tail() method
last_two = more_employees.tail(2)
print(f"last_two: {last_two}")

# Get the shape of a DataFrame
employee_shape = more_employees.shape
print(f"employee_shape: {employee_shape}")

# Use the info() method
print(more_employees.info())

# Task4: Data Cleaning
dirty_data = pd.read_csv("dirty_data.csv")
print(f"dirty_data: {dirty_data}")

clean_data = dirty_data.copy()

# Clean duplicates
clean_data.drop_duplicates(inplace=True)
print(f"after cleaning duplicates: {clean_data}")

# Convert Age to numeric and handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")

mean_age = clean_data["Age"].mean()
clean_data["Age"] = clean_data["Age"].fillna(mean_age)
print(f"replacing missing values with mean to pass the test \n: {clean_data}")

# Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print(f"clean_data after replacing and converting: \n {clean_data}")

median_salary = clean_data["Salary"].median()
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
print(f"clean_data after replacing salary median: \n {clean_data}")

# Convert Hire Date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], format='mixed', errors="coerce")
print(f"clean_data after converting to datetime: {clean_data}")

# Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Name"] = clean_data["Name"].str.upper()
clean_data["Name"] = clean_data["Name"].str.strip()

clean_data["Department"] = clean_data["Department"].str.upper()
clean_data["Department"] = clean_data["Department"].str.strip()
print(f"clean_data after Name and Department changed to uppercase\n: {clean_data}")