import functools
import time

# В бок от темы. Декоратор для измерения времени выполнения ф-ии
def stopwatch(func):
    def inner(*args, **kwargs):
        # print(func.__name__, args, kwargs)
        print(func.__name__)
        start = time.perf_counter()
        result =  func(*args, **kwargs)
        print(f"Evaluation: {time.perf_counter() - start}")
        return result
    functools.update_wrapper(inner, func)

    return inner
@stopwatch
def identity(x):
    "I do nothing useful"
    return x

