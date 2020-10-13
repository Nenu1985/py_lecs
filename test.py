import sys
import os

# first_string = sys.stdin.readline().strip()
# second_string = sys.stdin.readline().strip()

# N, X, K = [int(ch) for ch in first_string.split(' ')]
# t = [int(ch) for ch in second_string.split(' ')]


N, X, K  = [6,5,10]  # 1
N, X, K  = [5,7,12]  # 2



t = [1,2,3,4,5,6]  # 1
t = [5,22,17,13,8]  # 2
# t=[]

N, X, K  = [2,15,10]
t = [1,100]
t.sort()


def get_alarms_times(seen, T, X):
    s = set()

    for time in seen:
        k = 0
        time_to_add = time + X * k

        while time_to_add <= T:
            s.add(time_to_add)
            k += 1
            time_to_add = time + X * k

    return list(s)

def binary_search(alarms: list, required_times: int):
    mid = 0
    start = 0
    end = max(alarms or [0]) * K
    step = 0

    while (start <= end):
        mid = (start + end) // 2
        calc_times, set_of_rings = get_alarms_times(alarms, mid, X)
        print(f'BinSearch. {start=}, {end=}, {mid=}, {step=}, {calc_times=}')
        list_of_rings = list(set_of_rings)
        list_of_rings.sort()
        return list_of_rings[required_times - 1]
    #     if required_times == calc_times:
    #         return mid

    #     if required_times < calc_times:
    #         end = mid - 1
    #     else:

    #         start = mid + 1
    #     # step = step+1
    # return 0

# removing unnessessary alarms:
# seen = []
# for al in t:
#     if al % X not in seen:
#         seen.append(al)
#     else:
#         searhed_value = [a for a in seen if a % X == al % X][0]

#         idx = seen.index(searhed_value)
#         seen[idx] = min(searhed_value, al)

# print(f'Alarms: {seen=}')
n = max(t or [0]) * K

l= get_alarms_times(t, n, X)

l.sort()
# print(f'len={len(l)}. {l=}')
# tt = 1
# if len(l) >= K:
if len(l) >= K:
    print(l[K - 1])
else:
    print(0)





