"""
Function Decoraters : - 

        input function ---> Decorater Function ---> output Function with extended functionalityx    
        Decorater make our code shorter and pythonic
"""
def decor(func):
    def inner(name):
        if name == 'Mohit':
            print(f"Hello {name} very very good morning")
        else:
            func(name)
    return inner


@decor
def wish(name):
    print(f"Hello {name} Good Morning")



wish("Mohit")
wish("rohit")
wish("sohit")