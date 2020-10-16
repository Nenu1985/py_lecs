

import random

# from my_decorators import stopwatch, memory_profiler


def get_input_values(file):
    # with open(file, 'r') as file:
    #     lines = file.readlines()
    # a, b = lines[0].strip().split()
    examples = []
    N = int(input().strip())
    for i in range(N):
        examples.append(input())
    # examples = [
    #     '2*2=4',
    #     '25*25=625',
    #     '10+10=20',
    # ]

    # examples = [
    #     '2*2=5',
    # ]
    # examples = [
    #     '2*2=4',
    # ]
    # Z * Z = y1
    # int('Z', 36) * int('Z', 36) = 35 * 35 = 1225
    
    # examples = [
    #     'z*z=y1',
    # ]
    # examples = [
    #     'f*f=e1',
    # ]
    return examples

def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):

    (d, m) = divmod(number, base)
    if d > 0:
        # print('recursive call')
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)

def Multiply(num1, num2, base):
    answer = int(num1, base) * int(num2, base)
    return answer
def Sum(num1, num2, base):
    answer = int(num1, base) + int(num2, base)
    return answer
# @memory_profiler
# @stopwatch
def main():

    examples = get_input_values('input.txt')

    bases = []
    for example in examples:
        equetion, result = example.split('=')
        first_arg, second_arg, operation = equetion.split('*') + [Multiply] if '*' in equetion else equetion.split('+') + [Sum]
        'ord(A) = 65'
        min_base = max([int(ch) if ch.isdigit() else ord(ch.upper()) - ord('A') + 11 for ch in first_arg + second_arg + result])
        min_base = max(2, min_base)
        example_bases = set()
        for base in range(min_base, 37):
            check_result_base = operation(first_arg, second_arg, base)
            check_result_base_rebase = str_base(check_result_base, base)
            if check_result_base_rebase == result:
                example_bases.add(base)

        bases.append(example_bases)
    intersections = set()
    if len(bases) > 0:
        intersections = bases[0].intersection(*bases)
    if len(intersections) == 1:
        return list(intersections)[0]

    elif len(intersections) == 0:
       return 0
    else:  # len(intersections) > 1
        return -1
    # write_output_values('./output.txt', str(a + b))
    # print(a + b)
if __name__ == '__main__':
   ans = main()
   print(ans)
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