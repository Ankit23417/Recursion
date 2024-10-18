def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
print(factorial(6))
print(factorial(7))

print("Fibonacci Sequence")

def f(n):
    if (n == 1):
        return 1 
    elif(n == 0):
        return 0
    else:
        return f(n-1)+f(n-2)

print(f(9))
print(f(14))
print(f(5))
print(f(3))
