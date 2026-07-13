import os
import traceback

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the current working directory to the script's directory
os.chdir(script_dir)

try:
    with open("diary.txt", "a") as file:
        input_text = input("What happened today? ")
        while input_text.lower() != "done for now":
            file.write(input_text + "\n")
            input_text = input("What else?  ")
except KeyboardInterrupt:
    print("\nDiary entry interrupted by user.")
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")