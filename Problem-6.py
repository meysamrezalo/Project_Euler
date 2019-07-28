# AhriMAN

a = []
for i in range(1,101):
    b = i ** 2
    a.append(b)
 
b = 0

for c in a:
    b += c

n = 0

for o in range(1,101):
    n += o 
m = n ** 2
z = m - b

print('Sum squared 100 first digits :',b)
print('=============================================')
print('Sum of 100 numbers and squares it :' ,m)
print('=============================================')
print('''The difference between 
the two obtained above :''',z)

