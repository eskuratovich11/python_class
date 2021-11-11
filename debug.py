import functools
import math
 
def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [str(a) for a in args]
        kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Вызываем функцию {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"Функцию {func.__name__} вернула значение {value}")
        return value
 
    return wrapper_debug

debug_factorial = debug(math.sqrt)
 
def show_debug_function(terms=5):
    return [debug_factorial(n) for n in range(terms+1)]
 
show_debug_function(10)