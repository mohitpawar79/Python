"""
Bytes Data Type :  Bytes data type is immutale

Bytearray data type: Bytearray data type immutable

NOTE :  Both are same 
"""
x  = [1,2,3,4]
b  = bytes(x)
print(type(b))
print(b)

for i in b:
    print(i)


# #Bytes must be range 0 to 256 only 
# x  = [1,2,3,256]
# b  = bytes(x) # Getting Error


ba = bytearray(x)
print(ba)
print(ba[1])
ba[1] = 3
print(ba[1])

