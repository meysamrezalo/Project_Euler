#AhriMAN

num=600851475143
a=0
b=2
while b <= num:
	if num % b == 0:
		print(int(num),"is divisible", b)
		num = num / b
		a = b
	else:
		b = b + 1
print("The answer is the final :", a)