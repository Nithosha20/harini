def factorial_recursive(num):
    if num<=1:
        return 1
    return num*factorial_recursive(num-1)
v=factorial_recursive(5)
print(v)