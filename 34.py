a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
def gcd(a,b):
	return a if b==0 else gcd(b,a%b)
print("the greatest common divisor is ",gcd(a,b))
