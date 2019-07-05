number = int(input())
 
for j in range(2, number):
	if number % j  == 0:
		print("no")
		break
else:
	print("yes")
