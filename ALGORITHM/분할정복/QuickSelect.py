def kth_smallest_sort(A, k):
    A.sort()
    return A[k-1]

def quick_select(A, left, right, k):
    pos = partition(A, left, right)
    print(A)

    if (pos+1 == left+k):
        return A[pos]
    elif (pow+1 > left+k):
        return quick_select(A, left, pow-1, k)
    else:
        return quick_select(A, pos+1, right, k-(pos+1-left))
    
def partition(A, left, right):
    low = left + 1
    hight = right
    pivot = A[left]
    while (low <= high):
        while low <= right and A[low] <= pivot: 
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1

        if low < high:
            A[low], A[high], A[left]
    
    A[left], A[high] = A[high], A[left]
    return high