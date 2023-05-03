"""
Types Of varible :
    1.Global   --    the varible declare outside the function
                    this varible we can used in modeule
                    To make global varible inside function use global keyword ex. global var1
    2.Local    --    the varible declare inside the function
                    Local varible priority is highest
"""

a = 10
def fun1():
    print(a)
    print(globals()['a'])  # Use to access global varible without change local varible.    Global function return dict type with all varible which are global

def fun2():
    a = 100
    print(a)
    print(globals()['a'])  # Use to access global varible without change local varible


def fun3():
    global a
    a = 2
    print(a)

def fun4():
    print(a)

fun1()
fun2()
fun3()
fun4()