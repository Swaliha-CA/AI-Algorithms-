a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>=b and a>=c:
	print("Maximum is ",a)
elif  b>=a and b>=c:
	print("Maximum is ",b)
else:
	print("Maximum is ",c)
