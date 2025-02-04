def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
from powerMat import *
def fib_mat(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    mat = [[1, 1], [1, 0]]
    result = powerMat(mat, n)
    return result[0][1]

n = 31
print('Fibonacci(%d) 거듭제곱 = '%n, fib_mat(n))
print('Fibonacci(%d) 분할정복 = '%n, fib(n))