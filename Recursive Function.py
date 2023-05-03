"""
A function that call itself is called as recursive function.

advantages : we can reduce the length code
            and
            improves redablity
            we can solve complex problems very easily

"""
def factorial(a):
    if a == 0:
        fact = 1
    else:
        fact = a * factorial(a-1)
    return fact
print(factorial(9))



