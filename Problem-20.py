# AhriMAN

def factor(n):
    f = 1
    for x in range(n, 0, -1):
        f *= x
    return f

def p20(num):
    return sum([int(n) for n in str(factor(num))])

print(p20(100))