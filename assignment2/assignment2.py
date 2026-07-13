import csv 
import os
import traceback

from datetime import datetime

import custom_module


# Task2
def read_employees():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the parent directory of the script's directory
    parent_dir = os.path.dirname(script_dir)

    # Define the path to the employees.csv file in the csv folder
    employee_csv_path = os.path.join(parent_dir, "csv", "employees.csv")

    employees_data = {}
    rows = []

    try:
        with open(employee_csv_path, mode='r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    employees_data['fields'] = row
                    continue
                rows.append(row)
        
        employees_data['rows'] = rows
        return employees_data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    
        # Exact spelling and formatting requested by the spec
        print(f"An exception occurred. {type(e).__name__}")
        print(f"Stack Trace: {stack_trace}")


employees = read_employees()
print(employees)


# Task3
def column_index(column_name):
    if 'fields' not in employees:
        raise KeyError("Field data is not available.")

    try:
        return employees['fields'].index(column_name)
    except ValueError:
        raise ValueError(f"Column '{column_name}' not found.")

employee_id_column = column_index("employee_id")


# Task4
def first_name(row_number):
    c_idx = column_index("first_name")
    if "rows" not in employees:
        raise KeyError("Employee data is not available.")

    try:
        return employees['rows'][row_number][c_idx]
    except IndexError:
        raise IndexError(f"Row number {row_number} is out of range.")


# Task5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    if "rows" not in employees:
        raise KeyError("Employee data is not available.")

    matches = list(filter(employee_match, employees['rows']))
    return matches


# Task6
def employee_find_2(employee_id):
    if "rows" not in employees:
        raise KeyError("Employee data is not available.")
    
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees['rows']))
    
    return matches


# Task7
def sort_by_last_name():
    if "rows" not in employees:
        raise KeyError("Employee data is not available.")
    
    last_name_index = column_index("last_name")
    employees['rows'].sort(key=lambda row: row[last_name_index])
    return employees['rows']


sorted_employees = sort_by_last_name()
print(sorted_employees)


# Task8
def employee_dict(row):
    if "fields" not in employees:
        raise KeyError("Field data is not available.")
    
    empl_dict = {
        field: value
        for field, value in zip(employees["fields"], row)
        if field != "employee_id"
    }

    return empl_dict


empl_dict = employee_dict(employees["rows"][0])
print(empl_dict)
    

# Task9
def all_employees_dict():
    if "rows" not in employees:
        raise KeyError("Employee data is not available.")
    
    all_employees = {row[employee_id_column]: employee_dict(row) for row in employees['rows']}
    return all_employees


# Task10
def get_this_value():
    this_value = os.getenv("THISVALUE")
    if this_value is None:
        print("Environment variable 'THISVALUE' is not set.")

    return this_value


# Task11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)


set_that_secret("new_secret_value")
print(custom_module.secret)

# Task12
def read_minutes():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the parent directory of the script's directory
    parent_dir = os.path.dirname(script_dir)

    all_data = []
    for file_name in ["minutes1.csv", "minutes2.csv"]:
        file_path = os.path.join(parent_dir, "csv", file_name)

        data = {}
        rows = []

        with open(file_path, mode="r") as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                    continue
                rows.append(tuple(row))
        
        data["rows"] = rows
        all_data.append(data)

    return all_data[0], all_data[1]



minutes1, minutes2 = read_minutes()


# Task13
def create_minutes_set():
    if "rows" not in minutes1 or "rows" not in minutes2:
        raise KeyError("Minutes data is not available.")

    minutes_set = set(minutes1["rows"]) | set(minutes2["rows"])
    return minutes_set


minutes_set = create_minutes_set()


# Task14
def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))

    return minutes_list

minutes_list = create_minutes_list()
print(f"Minutes set: {minutes_list}")


# Task15
def write_sorted_list():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    sorted_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_list))

    csv_file_path = os.path.join(script_dir, "minutes.csv")

    if "fields" not in employees:
        raise KeyError("Field data is not available.")
    else:
        fields = minutes1["fields"]
    try:
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            for row in sorted_list:
                writer.writerow(row)
    except FileNotFoundError:
        print(f"File {csv_file_path} doesn't exist")
    except Exception as e:
        print(f"Exception happened {e}")
    
    return sorted_list
    

sorted_list = write_sorted_list()
