# task 2
import csv
import traceback
import custom_module

def read_employees():
    employees_dict = {}  
    rows = []  

    try:
        with open("csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    employees_dict["fields"] = row 
                else:
                    rows.append(row)  
        
        employees_dict["rows"] = rows 
        return employees_dict

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = [
            f'File: {trace[0]}, Line: {trace[1]}, Func.Name: {trace[2]}, Message: {trace[3]}'
            for trace in trace_back
        ]
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {str(e)}")
        print(f"Stack trace: {stack_trace}")
        exit(1)  


employees = read_employees()
print('Task2: ', employees)
print()

# task 3

def read_employees():
    
    data = {"fields": [], "rows": []} 

    try:
        with open("csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row  
                else:
                    data["rows"].append(row) 
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        return None  

    return data 

def column_index(column_name):
    
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"Column '{column_name}' not found.")
        return None

employees = read_employees()

if employees:  
    employee_id_column = column_index("employee_id")
    print(f"Task3: Employee ID Column Index: {employee_id_column}")
print()

# task 4

import csv

def read_employees():
    
    data = {"fields": [], "rows": []} 

    try:
        with open("csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row 
                else:
                    data["rows"].append(row)
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        return None  

    return data  

def column_index(column_name):
    
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"Column '{column_name}' not found.")
        return None

def first_name(row_number):
    
    first_name_col = column_index("first_name")  
    
    if first_name_col is None:
        return None  

    if 0 <= row_number < len(employees["rows"]): 
        return employees["rows"][row_number][first_name_col]  
    else:
        print("Invalid row number.")
        return None


employees = read_employees()


if employees:  
    print('Task4: ', first_name(3))  
print()

# task 5

def read_employees():
   
    data = {"fields": [], "rows": []}  

    try:
        with open("csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    data["fields"] = row 
                else:
                    data["rows"].append(row) 
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
        print(f"Exception message: {e}")
        return None 

    return data 

def column_index(column_name):
    
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"Column '{column_name}' not found.")
        return None

def employee_find(employee_id):
    
    
    def employee_match(row):
        
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))  
    return matches

employees = read_employees()

if employees:
    employee_id_column = column_index("employee_id")

if employees and employee_id_column is not None:
    print('Task5: ', employee_find(10))  
print()

# task 6

def employee_find_2(employee_id):
    
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    
    return matches
    
print('Task6: ',employee_find_2(3))
print()

# task 7
def sort_by_last_name():
    
    last_name_column = column_index("last_name")  
    employees["rows"].sort(key=lambda row: row[last_name_column])
    return employees["rows"]

print('Task 7: ', employees)
print()

# task 8

def employee_dict(row):
    
    employee_data = {}
    employee_id_column = column_index("employee_id") 

    
    for index, field in enumerate(employees["fields"]):
        if index != employee_id_column: 
            employee_data[field] = row[index]

    return employee_data

print (employee_dict(employees["rows"][5]))
print()

# task 9

def all_employees_dict():

    employees_data = {}
    employee_id_column = column_index("employee_id") 

    for row in employees["rows"]:
        employee_id = row[employee_id_column] 
        employees_data[employee_id] = employee_dict(row)

    return employees_data
print ('Task 9:', all_employees_dict())

# task 10
import os 

def get_this_value():
    return os.getenv("THISVALUE")


print('Task 10: ', get_this_value())  

# task 11

def set_that_secret(secret_value):
     custom_module.set_secret(secret_value)

set_that_secret("my_secret_value")

print('Task 11: ', custom_module.secret)
print()


# task 12

def read_csv_as_dict(filepath):
    try:
        with open(filepath, "r", newline="") as file:
            reader = csv.reader(file)
            data = {"fields": next(reader), "rows": [tuple(row) for row in reader]}
        return data
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return {"fields": [], "rows": []}

def read_minutes():
    minutes1 = read_csv_as_dict("csv/minutes1.csv")
    minutes2 = read_csv_as_dict("csv/minutes2.csv")
    return minutes1, minutes2


minutes1, minutes2 = read_minutes()

print("Task 12 Minutes1:", minutes1)
print("Task 12 Minutes2:", minutes2)
print()

# task 13

def create_minutes_set():
    set1 = set(minutes1["rows"]) 
    set2 = set(minutes2["rows"]) 
    return set1 | set2

minutes_set = create_minutes_set()

print("Task 13 Combined Minutes Set:", minutes_set)
print()

# task 14

from datetime import datetime

def create_minutes_list():
   
    minutes_list = list(minutes_set) 
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))

minutes_list = create_minutes_list()

print("Task 14 Minutes List:", minutes_list)
print()

# task 15

def write_sorted_list():
    global minutes_list

    
    minutes_list.sort(key=lambda x: x[1])

    formatted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))

   
    with open("./minutes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(formatted_list)

    return formatted_list

sorted_minutes = write_sorted_list()
print("Task 15 Sorted Minutes List:", sorted_minutes)





