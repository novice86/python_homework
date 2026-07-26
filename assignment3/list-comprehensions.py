import csv
import traceback


def read_employees():
    employees = []
    fields = []

    try:
        with open('../csv/employees.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    fields.extend(row)
                    continue

                employees.append(row)
        
        return fields, employees
    except Exception as e:
        print(f"An exception occurred. {type(e).__name__}")

        # Traceback formatting
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')

        print(f"Stack Trace: {stack_trace}")


def column_index(fields, column_name):
    try:
        return fields.index(column_name)
    except ValueError:
        raise ValueError(f"Column '{column_name}' not found.")


if __name__ == "__main__":
    fields, employees = read_employees()
    
    first_name_index = column_index(fields, "first_name")
    last_name_index = column_index(fields, "last_name")
    employee_names = [f"{row[first_name_index]} {row[last_name_index]}" for row in employees]
    print(employee_names)

    employee_names_filtered = [name for name in employee_names if "e" in name]
    print(employee_names_filtered)

