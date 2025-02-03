def find_max(A):
    n = len(A)
    max = A[0]
    for i in range(n):
        if A[i] > max:
            max = A[i]
    return max

def find_key(A, key):
    n = len(A)
    for i in range(n):
        if A[i] == key:
            return i
    return -1


data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("find_max: ", find_max(data))
print("find_key: ", find_key(data, 5))
print("find_key: ", find_key(data, 10))