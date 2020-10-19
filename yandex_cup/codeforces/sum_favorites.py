from itertools import repeat

'''
3
3 5
1 4 6
3 3
2 3 4
3 1000000000
1 2 3
'''
def get_input_values(file):
    # with open(file, 'r') as file:
    #     lines = file.readlines()
    # a, b = lines[0].strip().split()
    output = []
    N= input().strip() # number of tests:
    for i in range(int(N)):
        N, x= input().strip().split()
        secuence = input().strip().split()
        output.append((int(N), int(x), [int(s) for s in secuence]))
    return output

seq_glob = []

def get_sum_favirites_init(X, seq):
    return sum(-i if i in seq else i for i in range(1, X + 1))

class GetCondNumb:
    def __init__(self, seq) -> None:
        self.seq = seq
    def get_cond_num(self, num):
        return num if num not in self.seq else -num

def get_sum_favirites_map(X, seq):
    # s = 0
    obj = GetCondNumb(seq)
    ans = sum(map(obj.get_cond_num, range(1, X + 1)))
    return ans
from itertools import repeat

def get_sum_favirites_map2(X, seq):
    # s = 0
    obj = GetCondNumb(seq)
    compare = obj.get_cond_num

    ans = sum(map(compare, range(1, X + 1)))
    return ans

def get_sum_favirites_repeat(X, seq):
    ans = sum(map(lambda x, sequence: x if x not in sequence else -x, range(1, X + 1), repeat(seq, X)))
    return ans

def get_sum_favirites_lambda(X, seq):
    # global seq_glob
    seq_glob = seq
    ans = sum(map(lambda x: int(x) if x not in seq_glob else int(-x), range(1, X + 1)))
    return ans

def get_sum_fast(X, seq):
    filtered_seq = filter(lambda x: x <= X, seq)
    range_sum = int((X + 1)* X / 2)
    return range_sum - 2*sum(filtered_seq)
    # return sum(-i if i in seq else i for i in range(1, X + 1))
    # for i in range(1, X + 1):
    #     if i in seq:
    #         s += -i
    #     else:
    #         s += i
    # return s

def main():
    ans = ''
    in_data =  get_input_values('input.txt')
    for data in in_data:
        N, x, secuence = data
        ans += str(get_sum_fast(x, secuence)) + '\n'

    return ans

if __name__ == '__main__':
    main()

t = int(input())
while t:
    a, b = [int(i) for i in input().split(' ')]
    common = a | b
    min_sum = a ^ x + b ^ x
    print(min_sum)
    t-=1