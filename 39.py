string=input("Enter the string:")
print("Reversed string:",string[::-1])
print("the string is palindrome" if string==string[::-1] else"Not a palindrome")
