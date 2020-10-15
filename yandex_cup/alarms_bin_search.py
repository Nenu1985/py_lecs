from collections import Counter
import time
import random
from decorators import stopwatch
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

200 350 5000
19 72 97 198 363 301 429 41 140 84 11 94 298 448 430 151 23 473 451 183 74 137 202 147 196 476 272 486 414 469 239 167 431 147 339 198 90 494 294 397 343 322 9 427 339 184 215 109 284 319 100 14 327 331 325 75 113 101 2 15 70 81 35 325 389 69 398 91 271 140 488 368 242 232 377 495 23 155 293 331 103 107 132 367 451 465 260 237 252 146 310 373 483 222 71 246 473 177 338 422 200 474 243 69 434 212 62 136 246 449 131 186 369 156 392 162 282 250 294 125 340 388 434 96 419 331 411 414 267 262 79 258 458 184 282 445 389 477 404 468 461 111 442 187 453 420 93 67 28 240 359 492 153 260 431 248 13 418 90 15 149 26 227 4 192 105 402 266 272 288 13 358 412 95 80 402 86 304 487 220 451 405 31 328 482 294 198 284 409 115 362 185 192 214 206 320 90 392 382 342
 ' '.join([str(random.randrange(1,500)) for i in range(200)])   # to generate t's
https://pypi.org/project/memory-profiler/
python -m memory_profiler alarm_bin_search.py 
'''
# @profile
@stopwatch
def get_input_values(file):
    with open(file, 'r') as file:
        lines = file.readlines()
    N, X, K = lines[0].strip().split()
    t = lines[1].strip().split()
    # t =  ' '.join([str(random.randrange(1,50000)) for i in range(1000000)])   # to generate t's
    t = [random.randrange(1,50000) for i in range(1000000)]
    return int(N), int(X), int(K), [int(time) for time in t]

def get_alarms_times(alarms, T, X):
    # times = []

        # times.extend(a + X*i for i in range((T -a) // X + 1))
    return sum((T - a) // X + 1 for a in alarms if a <= T)
    
# @profile
@stopwatch
def get_filtered_alarms(alarms, X, start_time, timer_times):
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
@stopwatch
def main():
    _, X, K, t = get_input_values('input.txt')

    timer_times = []
    start_time = time.time() # start
    filtered_alarms = get_filtered_alarms(t, X, start_time, timer_times)

    # if X > 100:
    #     raise ModuleNotFoundError(f'K={K}, X={X}, t={t}')
    start = min(t)
    end = 100

    if X == 0:
        end = len(t) * K + 1
    else:
        end = K * X + min(t) + 1
    while True:

        mid = (end + start) // 2
        # print(f'{mid}, {start} {end}')
        times = get_alarms_times(filtered_alarms, mid, X)
        # iter_time =  time.time() - start_time
        # timer_times.append(iter_time) # filtered
        # if iter_time > 1.5:
        #     raise TimeoutError(f'K={K}, X={X}, t={t}, timer_times={timer_times} start={start}, end={end}')
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
