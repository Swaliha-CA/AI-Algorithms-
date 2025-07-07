n=int(input("Enter the number:"))
def is_palindrome(n):
	return str(n)==str(n)[::-1]
print(is_palindrome(n))
