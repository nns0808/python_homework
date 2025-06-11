import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        pos_args = list(args) if args else "none"
        kw_args = kwargs if kwargs else "none"
        result = func(*args, **kwargs)
        log_message = (
            f"function: {func_name} "
            f"positional parameters: {pos_args} "
            f"keyword parameters: {kw_args} "
            f"return: {result}"
        )
        logger.log(logging.INFO, log_message)
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def check_all_true(*args):
    return True

@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    check_all_true(1, 2, 3)
    return_decorator(key1="value1", key2="value2")
