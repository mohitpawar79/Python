"""
List :  - Insertion order is preserved 
        - Duplicates are allowed
        - Muteble data type  
        - Hetrogenius Object are allowed (Diffrent Objects)  
        - values should be enclosed with []
"""

l = [] 
print(type(l))

l.append(10) # To add value in list
print(l)
l.append(30)
print(l)
l.append(2)
print(l)

l.append(None)
print(l)

print(l[1:])
print(l[:-1])

print(l[1:3:2])

