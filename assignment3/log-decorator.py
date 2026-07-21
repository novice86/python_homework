# Task1
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler(
    filename="./decorator.log",
    mode="a",
    encoding="utf-8")
)

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        output_value = func(*args, **kwargs)
        log_message = (
            f"function: {func.__name__}\n"
            f"positional parameters: {args if args else 'none'}\n"
            f"keyword parameters: {kwargs if kwargs else 'none'}\n"
            f"return: {output_value}"
        )
        logger.log(logging.INFO, log_message)

        return output_value
    
    return wrapper


@logger_decorator
def hello_world():
    print("Hello world!")


@logger_decorator
def func_with_positional_args(*args):
    print(args)
    return True


@logger_decorator
def func_with_keyword_args(**kwargs):
    return logger_decorator


hello_world()
func_with_positional_args(1, 2, 3)
func_with_keyword_args(param1=1, param2=2, param3=3)