#AhriMAN

P2,fib,f1,f2 = 0,0,1,0
debugP2 = []

while fib < 4000000:
    fib = f1 + f2
    f2 = f1
    f1 = fib
    if fib % 2 == 0:
        P2 += fib
        debugP2.append(fib)
        
#print(debugP2)
print([P2])