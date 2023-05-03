dic = dict([(1,"Mohit"),(2,"Nitin")])
print(dic)
dic[3] = "Raj"
print(dic.values())   #For values
print(dic.keys())     #for keys
print(dic.items())    #for items

for i in dic.keys():
    print(i)

for i in dic.values():
    print(i)

for i,j in dic.items():
    print(i , "      ", j)
