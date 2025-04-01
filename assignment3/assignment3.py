# Task 1.1
import pandas as pd

myDict = {
    'Name': ['Alice', 'Bob', 'charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(myDict)

print('Task 1.1 ', task1_data_frame)
print()

# Task 1.2
task1_with_salary = task1_data_frame.copy()

task1_with_salary["Salary"] = [70000, 80000, 90000]

print('Task 1.2 ', task1_with_salary)

# Task 1.3
task1_older = task1_with_salary.copy()
task1_older ["Age"] += 1

print ('Task 1.3 ',task1_older)

# Task 1.4
task1_older.to_csv("employees.csv", index=False)

print()

# Task 2.1

task2_employees = pd.read_csv("employees.csv")

print('Task 2.1 ', task2_employees)
print('Task 2.1 ', task2_employees.columns)
print('Task 2.1', task2_employees.info())
print()

# Task 2.2
json_employees = pd.read_json('additional_employees.json')
print('Task 2.2 ', json_employees)
print()

# Task 2.3

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)

print('Task 2.3 ', more_employees)
print()

# Task 3.1
first_three = more_employees.head(3)

print('Task 3.1 ', first_three)
print()

# Task 3.2
last_two = more_employees.tail(2)
print('Task 3.2 ', last_two)
print()

# Task 3.3
employee_shape = more_employees.shape
print('Task 3.3 ', employee_shape)
print()


# Task 3.4
print('Task 3.4')
more_employees.info()
print()

# Task 4.1
dirty_data = pd.read_csv("assignment3/dirty_data.csv")  

print(dirty_data)  

clean_data = dirty_data.copy()  
print('Task 4.1 ', clean_data)
print()

# Task 4.2
clean_data = clean_data.drop_duplicates()

print('Task 4.2 ',clean_data) 
print()

# Task 4.3
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

clean_data['Age'].fillna(clean_data['Age'].mean(), inplace=True)  

print('Task 4.3 ', clean_data)
print()

# Task 4.4

import numpy as np

clean_data['Salary'].replace(["unknown", "n/a"], np.nan, inplace=True)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

print('Task 4.4 ', clean_data)
print()

# Task 4.5
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())

print('Task 4.5 ', clean_data)
print()

# Task 4.6
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors="coerce")

print('Task 4.6 ', clean_data)
print()

# Task 4.7
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()

print('Task 4.7 ', clean_data)
