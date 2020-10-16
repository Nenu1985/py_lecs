'''
Даны два числа A и B. Вам нужно вычислить их сумму A+B. 
В этой задаче для работы с входными и выходными данными вы можете использовать и файлы и потоки на ваше усмотрение.
'''

import random
import time
import tracemalloc
from collections import Counter

from my_decorators import stopwatch




@stopwatch
def get_input_values(file):
    with open(file, 'r') as file:
        lines = file.readlines()
    N, X, K = lines[0].strip().split()
    t = lines[1].strip().split()
    t =  ' '.join([str(random.randrange(1,50000)) for i in range(1000000)])   # to generate t's


    


# @profile
@stopwatch
def main():
    tracemalloc.start()
    _, X, K, t = get_input_values('input.txt')

    current, peak = tracemalloc.get_traced_memory()
    print(f'Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB')
    tracemalloc.stop()


if __name__ == '__main__':
    main()
