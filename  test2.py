from collections import Counter
import time
'''
5 7 12
5 22 17 13 8

6 5 10
1 2 3 4 5 6

6 130 1342254
1 500 200000 11111111 231321 21546


2 7 50
1 2 

5 7000 120
5 22 17 13 8

https://pypi.org/project/memory-profiler/
python -m memory_profiler alarm_bin_search.py 
'''
# @profile
def get_input_values(file):
    with open(file, 'r') as file:
        lines = file.readlines()
    N, X, K = lines[0].strip().split()
    t = lines[1].strip().split()
    return int(N), int(X), int(K), [int(time) for time in t]

def get_alarms_times(alarms, T, X):
    # times = []

        # times.extend(a + X*i for i in range((T -a) // X + 1))
    return sum((T - a) // X + 1 for a in alarms if a <= T)

# @profile
def get_filtered_alarms(alarms, X, start_time):
    filtered_alarms = []
    alarms.sort()

    a = {v: v % X for v in alarms}
    b = Counter(a.values())

    # k = ostatok, v = count
    ostatki = [k for k, v in b.items() if v > 1]
    unique = [k for k, v in b.items() if v == 1]

    [filtered_alarms.append(k) for k, v in a.items() if v in unique]

    for ostatok in ostatki:

        same_alarms = [k for k, v in a.items() if v == ostatok]
        filtered_alarms.append(same_alarms[0])

    return filtered_alarms

# @profile
def main():
    _, X, K, t = get_input_values('input.txt')
    # timer_times = []
    start_time = time.time() # start
    filtered_alarms = get_filtered_alarms(t, X, start_time)

    # if X > 100:
    #     raise ModuleNotFoundError(f'K={K}, X={X}, t={t}')
    start = min(t)
    # end = 100
    # if K > 1000000:
    #     raise RuntimeError('afs')
    # while get_alarms_times(filtered_alarms, end, X) < K:
    if X == 0:
        end = len(t) * K + 1
    else:
        end = K * X + min(t) + 1
        # iter_time =  time.time() - start_time
        # if iter_time > 2.0:
        #     raise RuntimeError(f'K={K}, X={X}, t={t} start={start}, end={end}')
    while True:

        mid = (end + start) // 2
        # print(f'{mid}, {start} {end}')
        times = get_alarms_times(filtered_alarms, mid, X)
        # iter_time =  time.time() - start_time
        # timer_times.append(iter_time) # filtered
        # if iter_time > 1.5:
        #     c
        # print(f'times = {times}')
        if times == K and start == end and start == end:

            print(mid)
            return
        elif times < K:
            start = mid + 1

        else:
            end = mid


if __name__ == '__main__':
    main()
