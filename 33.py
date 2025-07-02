n=int(input("Enter the number:"))
def sum_digits(n):
	return 0 if n==0 else n%10+sum_digits (n//10)
print(sum_digits(n))
