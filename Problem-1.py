#AhriMAN

from functools import reduce

a = []

for i in range(1,1000):
    if i % 3 == 0:
        a.append(i)
    elif i % 5 == 0:
        a.append(i)
        
n = reduce(lambda x,y: x+y , a)

#print(a)
print([n])