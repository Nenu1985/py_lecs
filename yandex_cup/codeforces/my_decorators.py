import functools
import time
import tracemalloc

# В бок от темы. Декоратор для измерения времени выполнения ф-ии
def stopwatch(func):
    def inner(*args, **kwargs):
        # print(func.__name__, args, kwargs)
        print(func.__name__)
        start = time.perf_counter()
        result =  func(*args, **kwargs)
        print(f"Evaluation: {time.perf_counter() - start:f}")
        return result
    functools.update_wrapper(inner, func)

    return inner

def memory_profiler(func):
    def inner(*args, **kwargs):
        tracemalloc.start()
        print('Memory measurement:', func.__name__)

        result =  func(*args, **kwargs)
        
        current, peak = tracemalloc.get_traced_memory()
        print(f'Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB')
        tracemalloc.stop()
        return result
    functools.update_wrapper(inner, func)

    return inner

@stopwatch
def identity(x):
    "I do nothing useful"
    return x

