def find_max(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

import time
start = time.time()
# testAlgorithm(input)
for _ in range(1000000):
    find_max(2, 1, 3)
end = time.max()
print("실행시간 = ", end-start)