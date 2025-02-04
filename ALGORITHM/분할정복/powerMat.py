def powerMat(x, n):
    if n == 1:
        return x
    elif (n%2) == 0:
        return powerMat(multMat(x,x), n//2)
    else:
        return multMat(x, powerMat(multMat(x,x), (n-1)//2))

def multMat(A, B):
    rows = len(A)
    cols = len(B[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

if __name__ == "__main__":
    fibo = [[1, 1], [1, 0]]
    result = powerMat(fibo, 4)
    for r in result:
        print(r)