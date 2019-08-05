# Ahriman

num = 1
number = []
while True:
    NUM = num  
    a , b , c , d , f = num * 2 , num * 3 , num * 4 , num * 5 , num * 6
    num1 , a1 , b1 , c1 , d1 , f1 = str(num) , str(a) , str(b) , str(c) , str(d) , str(f)
    num2 , a2 , b2 , c2 , d2 , f2 = list(num1) , list(a1) , list(b1) , list(c1) , list(d1) , list(f1)
    num2.sort() , a2.sort() , b2.sort() , c2.sort() , d2.sort() , f2.sort()
    if a2 == num2:
        num += 1
        if b2 == num2:
            num += 1
            if c2 == num2:
                num += 1
                if d2 == num2:
                    num += 1
                    if f2 == num2:
                        number.append(NUM)
                        break
    else:
        num += 1

print(number)    
