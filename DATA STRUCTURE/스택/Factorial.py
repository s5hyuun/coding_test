def factorial_iter(n):
    result = 1
    for k in range(2, n+1):
        result = result * k
    return result

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print('Factorial순환(3) = ', factorial(3))
print('Factorial반복(3) = ', factorial_iter(3))

print('Factorial순환(10) = ', factorial(10))
print('Factorial반복(10) = ', factorial_iter(10))

a = 10
print(type(a)) # int

a = 10.0
print(type(a)) # float
print(type(123)) # int
print(type(123.0)) # float
print(type("123")) # str
print(type(True)) # bool
print(type(1+2j)) # complex