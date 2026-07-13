import os
import traceback


try:
    with open("diary.txt", "a") as file:
        # Set the initial prompt text
        prompt_text = "What happened today? "
        
        while True:
            input_text = input(prompt_text)
            
            # Check for the exit condition
            if input_text == "done for now":
                file.write("done for now\n")
                break
            
            # Write standard entries with a newline
            file.write(input_text + "\n")
            
            # Update the prompt text for all subsequent loops
            prompt_text = "What else? "

# Catch the general Exception as requested
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    
    # Exact spelling and formatting requested by the spec
    print(f"An exception occurred. {type(e).__name__}")
    print(f"Stack Trace: {stack_trace}")
