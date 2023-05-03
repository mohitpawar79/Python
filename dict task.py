# WAP to take a dict from keybord and dislplay the sum of value

dic =  {}
flag = 1

while True:
    key = eval(input("Enter Key : "))
    value = eval(input("Enter Value : "))
    dic[key] = value
    flag = eval(input("For add one more press 1 "))
    if flag != 1:
        break
print("Your Dict is : ",dic)
print("Total of values is : ",sum(dic.values()))

