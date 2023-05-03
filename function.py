"""
function is a collection of statement

Syntax

def function_name()
def function_name(parameters)

Tupes of function :

User define                     System Define



if the function is define outside of class then its knows as function

if the function define inside class then its known as method


parameters -
    1.Positional Argument : Number of arguments is IMp
                            Order is also Important
                            def cac(a,b):
                                print("Sum is {} ".format(a+b))
                            cac(10,20)

    2.Key-word Argument : Order is not Important
                          Number of arguments is IMp
                            def cac(a,b):
                                print("Sum is {} ".format(a+b))
                            cac(b=10,a=20)

    3.Default Arguments : Default argument always declare in last

                         def cac(b,a=10):
                                print("Sum is {} ".format(a+b))
                         cac(20)

    4.Varible length argument :Below method is known as varinble length arguments
                            : Internally the paramenter is TUPLE
                            def sum(*a):




"""
# #  Example
#
# def cac(name, *a):
#     result = 0
#     for i in a:
#         result +=i
#     print("Sum by {name} is {sum} ".format(name=name,sum=result))
#
#
# cac("Mohit ",10,20)
# cac("Mohit ",10,2,200,3)
# cac("Mohit ",12,2,2,2,2,2,2,2,2,2,2,2)


def family(**kargs):
    for k,v in kargs.items():
        print(k , "      ",v)
family(name="mohiy",age=21)