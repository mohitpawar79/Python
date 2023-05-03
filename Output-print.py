print(10,20,30,sep=":")   #sep opratpr
print(10,20,30,end=" ")   #end opratpr
print(10,20,30,sep=":")   #sep opratpr

"""
%i and %d is use for int 
%f is use for float
%s is use for str
"""

a,b = 10,20
print("Value of a is %i"%a)
print("Value of a is %i and value of b is %i"%(a,b))

# Replacement operator {}

name = "Mohit Dhangar"
print("my name is {}".format(name))

school = "rcp"
print("my name is {} and school is {}".format(name,school))
print("my name is {name} and school is {school}".format(school=school,name=name))
