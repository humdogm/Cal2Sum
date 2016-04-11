from math import log
sum = float(0)
for i in range(1,11):
	sum += float(5/(2**i))
print(sum+float((5*(2**(-10))/log(2))))
print(sum+float((5*(2**-(11))/log(2))))