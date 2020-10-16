import random
import time
import tracemalloc
from collections import Counter
import array
import bisect
from my_decorators import stopwatch

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

Init values:
    TIME = 12.2 sec
    MEMORY_peak = 45.2 MB


Optimisation: 
1. replace list comprehension to generator

'''
# @profile
@stopwatch
def get_input_values(file):
    # with open(file, 'r') as file:
    #     lines = file.readlines()
    # N, X, K = lines[0].strip().split()
    # t = lines[1].strip().split()
    # t =  ' '.join([str(random.randrange(1,50000)) for i in range(1000000)])   # to generate t's
    N, X, K  = (10000, 350, 5000000000000)
    # t = [random.randrange(1,50000) for _ in range(1000000)]  # 1
    t = random.sample(range(1, 100000000), 50000)
    return int(N), int(X), int(K), t

    
class GetAlarmTimes:
    def __init__(self, alarms, X_interval, K_times_required):
        self.start = min(alarms)
        self.end = K_times_required * X_interval + min(alarms) + 1 if X_interval > 0 else len(alarms) * K_times_required + 1
        self.x_interval = X_interval
        self.alarms = alarms

    def __len__(self):
        return sum((self.end - a) // self.x_interval + 1 for a in self.alarms if a <= self.end)

    def __getitem__(self, position):
        return sum((position - a) // self.x_interval + 1 for a in self.alarms if a <= position)

# @profile
@stopwatch
def get_filtered_alarms(alarms, X, start_time, timer_times) -> list:
    filtered_alarms = []
    # alarms = sorted(alarms)
    alarms.sort()

    a = {v: v % X for v in alarms}
    b = Counter(a.values())

    ostatki = [k for k, v in b.items() if v > 1]
    unique = [k for k, v in b.items() if v == 1]

    filtered_alarms = [k for k, v in a.items() if v in unique]

    for ostatok in ostatki:

        filtered_alarms.append([k for k, v in a.items() if v == ostatok][0])
        # filtered_alarms.append(same_alarm)

    return filtered_alarms

# @profile
@stopwatch
def main():
    tracemalloc.start()
    _, X, K, t = get_input_values('input.txt')

    timer_times = []
    start_time = time.time() # start
    filtered_alarms = get_filtered_alarms(t, X, start_time, timer_times)

    # if X > 100:
    #     raise ModuleNotFoundError(f'K={K}, X={X}, t={t}')
    get_alarm_times = GetAlarmTimes(filtered_alarms, X, K)
    print(bisect.bisect_left(get_alarm_times, K))
    current, peak = tracemalloc.get_traced_memory()
    print(f'Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB')
    tracemalloc.stop()


if __name__ == '__main__':
    main()
