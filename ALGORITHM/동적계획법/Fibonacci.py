def fib_dp_mem(n):
    if mem[n] == None:
        if n < 2:
            mem[n] = n
        else:
            mem[n] = fib_dp_mem(n-1) + fib_dp_mem(n-2)
    return mem[n]

def fib_dp_tab(n):
    f = [None] * (n+1)
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_iter(n):
    if (n < 2):
        return n
    last = 0
    current = 1
    for i in range(2, n+1):
        tmp = current
        current += last
        last = tmp
    return current

n = 8
print('Fibonacci(%d) 분할정복= '%n, fib(n))
print('Fibonacci(%d) 테이블화= '%n, fib_dp_tab(n))
mem = [None] * (n+1)
print('Fibonacci(%d) 메모이제이션= '%n, fib_dp_mem(n))
print('Fibonacci(%d) 반복구조= '%n, fib_iter(n))