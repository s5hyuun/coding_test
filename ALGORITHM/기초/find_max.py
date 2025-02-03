def find_max(a, b, c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    return max

print("find_max(1, 2, 3) = ", find_max(1, 2, 3))
print("find_max(3, 2, 1) = ", find_max(3, 2, 1))
print("find_max(2, 1, 3) = ", find_max(2, 1, 3))