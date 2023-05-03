
# -----------------------------------------------------int()-----------------------------------------------------

# Convert str,bool and float to int      : int()   : any oyher value to int type       !--- You can't convert complex data type to int  ex. int(10 + 12j)
print(int("20") , "  ", int(2.2), "  ", int(True))

# -----------------------------------------------------float()-----------------------------------------------------

# Convert int, bool and str to float      : float()                                    !--- You can't convert complex data type to float  ex. float(10 + 12j)
print(float(10), "  " , float(True), "   ", float("10.2"))

# -----------------------------------------------------complex()-----------------------------------------------------

# other type's  to Complex
    # Form - 1 : complex(x) == > x + 0j     x is real part
    # Form - 2 : Complex(x,y) == > x +yj    x is real and y is imagneary part
#Form 1 : 
print(complex(10))     # From int to comlex
print(complex(True))   # From bool to compplex
print(complex("10"))   # From str to complex
print(complex(10.4))   # From float to complex

#Form 2 : 
print(complex(10,5))
print(complex(True,False))
print(complex(10,5.4))
# -----------------------------------------------------bool()-----------------------------------------------------

# other type's to bool : 

print(bool(0))          # 0 means false only other all values are true
print(bool(0.0))        # in 0.0 case value is false else all values are true
print(bool(""))         # if string is empty then value is false else true
print(bool(0 + 0j))     # If both  the real and imagenry  part is 0 then result is false else true

# -----------------------------------------------------str()-----------------------------------------------------

#Other type to string

print(str(1))
print(str(1.1))
print(str(True))
print(str(10+0j))


x = 10
y = 10
one = 1
x1 =12

print("True" if id(x) == id(y) else "False")  # If the content of object is same then id of both object is same
