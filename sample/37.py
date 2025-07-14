s=input("Enter the string:")
v,c=0,0
vowels="AEIOUaeiou"
for ch in s:
	if ch.isalpha():
		if ch in vowels:
			v+=1
		else:
			c+=1
print("VOWELS:",v,"CONSONANTS:",c)
