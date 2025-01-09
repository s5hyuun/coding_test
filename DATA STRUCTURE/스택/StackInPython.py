s = list()

msg = input("문자열 입력: ")
for c in msg:
    s.append(c)

print("문자열 출력: ", end='')
while len(s) > 0:
    print(s.pop(), end='')
print()

import queue

s = queue.LifeQueue(maxsize=100)

msg = input("문자열 입력: ")
for c in msg:
    s.put(c)

print("문자열 출력: ")
while not s.empty():
    print(s.get(), end='')
print()