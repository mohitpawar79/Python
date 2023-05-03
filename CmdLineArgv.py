import sys


argv = sys.argv[1:]
sum = 0

for i in argv:
    sum += int(i)
print(sum)