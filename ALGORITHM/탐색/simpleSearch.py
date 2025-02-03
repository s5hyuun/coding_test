def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            return i
    return -1

def sequential_search_transpose(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            if i > low:
                A[i], A[i-1] = A[i-1], A[i]
                i = i - 1
            return i
    return -1

def binary_search(A, key, low, high):
    if (low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif (key < A[middle]):
            return binary_search(A, key, low, middle-1)
        else:
            return binary_search(A, key, middle+1, high)
    return -1

def binary_search_iter(A, key, low, high):
    while (low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif (key > A[middle]):
            low = middle + 1
        else:
            high = middle - 1
    return -1

# 보간탐색 중앙요소 위치
# middle = low + (high - low) * (key - A[low].key) / (A[high].key - A[low].key)

array = [3, 9, 15, 22, 31, 55, 67, 88, 91]
n = len(array)

print("입력배열 = ", array)
number = int(input("탐색할 숫자를 입력하세요: "))

print("순차 탐색: ", sequential_search(array, number, 0, n-1))
print("이진 탐색: ", binary_search(array, number, 0, n-1))
print("이진 반복: ", binary_search_iter(array, number, 0, n-1))