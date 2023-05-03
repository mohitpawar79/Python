"""
Imp methods for interviwe
"""
# 1 . Filter   :  is use for  : you have 20 number and find odd numbers


"""
filter syntax : 
    filter(function, sequence)          #  May be list or tuple or set 
                                        # Every element of sequence is applied for finction which is parameter of filter , method
                                        # IF the function returnes true then value is select
                                        # If the function return false then value is ignored
                                        # Only check True or False
                                        # Filter method return alwayes filter object type 
      
"""

def  isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False
l = [1,2,3,4,5,5,6,7,8,8,12,23,33,23,212,34]
even = list(filter(isEven,[i for i in range(100)]))                                  # Always check True or False

print(even)

# Using lambda

odd = list(filter(lambda x : x % 2 != 0, l))

print(odd)

# ------------------------------------------------------------------------------------------------------------------------------

# 2 . Map() Function

"""
Map syntax : 
    map(function, sequence)    
    
    use to do operation on sequence
    use to apply business logic on sequence 
    its always return values 
    we can apply map function on multiple function but bot sequence element kength is same 
"""
def squere(x):
    return x**2

l = list(map(squere,[i for i in range(1,11)]))           # Create a new list with business logic using fun
print(l)

l = list(map(lambda x : x**2,[i for i in range(1,11)]))           # Create a new list with business logic using lambda
print(l)


# we can apply map function on multiple function but bot sequence element kength is same

l = list(map(lambda x,y: x*y,[i for i in range(1,11)],[i for i in range(11,21)]))
print(l)

l = list(map(lambda x,y,z: x*y*z,[i for i in range(1,11)],[i for i in range(11,21)],[i for i in range(11,21)]))
print(l)



l = list(map(lambda x:'+ve' if x%2==0 else '-ve' ,[i for i in range(1,11)]))           # Create a new list with business logic 
print(l)



#Reduce Function :   return the only one value of sequence 

# ex . 
from functools import reduce
l = [1,2,3,4,5,6,7,8]
result = reduce(lambda x,y : x+y, l)

print(result)