import math
d = map(int,raw_input().split(','))
x = ""
for dx in d:
    x=x+str(int(math.sqrt(10.0/3*dx)))+','
print x[:len(x)-1]
