'''a= "my name is {} i am from {}"
b = "india"
c="ankit"
print(a.format(c,b))
print(f"my name is {c} i am from {b}")'''

txt = "for only{price:.2f}doller"
print(txt.format(price = 874.3333333))
 
print(f"{{c}}")


def add(a,b): 
    return a+b

a = 2 
b = 3
print(add(a,b))

# def factorial(n):
#     if (n == 0 or n == 1):
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))
# print(factorial(6))
# print(factorial(7))

def f(n):
    if (n == 1):
        return 1 
    elif(n == 0):
        return 0
    else:
        return f(n-1)+f(n-2)

print(f(6))