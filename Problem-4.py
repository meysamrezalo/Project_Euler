# AhriMAN

# [x] and [y] list for storing numbers from loops

x = []
for a in range(900,999): #Variable suffering (900,999)
	for b in range(900,999): #Variable suffering (900,999)
		f = a * b
		x.append(f)
#print(x)

y = []
for a1 in x:
	''' 
	The number of digits 
	stored in the list (x) should
	 be small or large manually
	 '''
	b1 = a1
	a1 , q = a1 // 10 , a1 % 10
	a1 , w = a1 // 10 , a1 % 10
	a1 , e = a1 // 10 , a1 % 10
	a1 , r = a1 // 10 , a1 % 10
	a1 , t = a1 // 10 , a1 % 10
	a1 , q , w , e , r , t = str(a1),str(q),str(w),str(e),str(r),str(t) 
	z = q + w + e + r + t + a1
	Z = int(z)
	if b1 == Z:
		y.append(Z)

print('==================================================')
print('''Palindrome available in range 900,999 :
''' , y[5:])
print('==================================================')
print('''The largest palindrome built with two
3-digit numbers :''', [max(y)])
print('==================================================')