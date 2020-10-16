def get_input_values(file):
    # with open(file, 'r') as file:
    #     lines = file.readlines()
    # a, b = lines[0].strip().split()

    A = input().strip()
    B = input().strip()

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
    return A, B


def main():

    A, B = get_input_values('input.txt')
    if '(' in A:
        A[A.find("(")+1: A.find(")")]
    if '(' in B:
        number_part, drob_part = B.split('.')
        drob_begin_part = drob_part[:drob_part.find("(")]
        z = B[B.find("(")+1:B.find(")")]
        drob_begin_part += z * (8 // len(z) + 1)
        float(f'{number_part}.{drob_begin_part}')


    str = f'{12:-5}, asf'
    A.find('(')
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
