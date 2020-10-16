

import random

# from my_decorators import stopwatch, memory_profiler


def get_input_values(file):
    # with open(file, 'r') as file:
    #     lines = file.readlines()
    # a, b = lines[0].strip().split()
    a, b = input().strip().split()
    return int(a), int(b)

def write_output_values(file, data: str) -> None:
    with open(file, 'w') as file:
        file.write(data)

# @memory_profiler
# @stopwatch
def main():


    a, b = get_input_values('input.txt')
    # write_output_values('./output.txt', str(a + b))
    print(a + b)
if __name__ == '__main__':
    main()
'''
def get_input_values(file: str):
    with open(file, 'r') as file:
        lines = file.readlines()
    a, b = lines[0].strip().split()
    return int(a), int(b)

def write_output_values(file: str, data: str) -> None:
    with open(file, 'wb') as file:
        file.write(data.encode())

# @memory_profiler
# @stopwatch
def main():

    a, b = get_input_values('input.txt')
    write_output_values('./output.txt', str(a + b))
    '''