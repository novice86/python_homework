# Task2
def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            output = func(*args, **kwargs)
            if type_of_output == "str": 
                return str(output)
            elif type_of_output == "float":
                return float(output)
            elif type_of_output == "int":
                return int(output)
        return wrapper
    
    return decorator


@type_converter("str")
def return_int():
    return 4


@type_converter("int")
def return_string():
    return "not a number"


y = return_int()
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen