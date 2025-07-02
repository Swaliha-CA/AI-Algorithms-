#when using with you don't want to close it.
#file handling
'''with open("file.txt","r") as f:
	print(f.read())'''
	
'''with open("file.txt","w") as f:
	f.write("WELCOME TO MY CHANNEL")'''
	
'''with open("file.txt","a") as f:
	f.write("THIS IS MY FIRST FILE")'''
	
#count wordsin a file
'''with open("file.txt") as f:
	words=f.read().split()
print("word count:",len(words))'''


#count lines in a file
'''with open("file.txt") as f:
	print("line count:",len(f.readlines()))'''
	
	
'''with open("file.txt") as f:
	lines=f.readlines()
	print(lines)
	print("lines count:",len(lines))'''
	


 #merge contents of 2 files
'''with open("f1.txt") as f1,open("f2.txt") as f2:
	with open("f3.txt","w") as f3:
		f3.write(f1.read()+f2.read())
		'''


#Handle file not found
'''try:
	with open("f4.txt") as f:
		print(f.read())
except FileNotFoundError:
	print("FILE NOT FOUND")'''


#division by zero
'''
try:
	a=12/0
except ZeroDivisionError:
	print("Dividing by zero not possible")
'''

#value error
'''try:
	x=int(input("Enter number:"))
except ValueError:
	print("invalid input!")
else:
	print("valid input!")
finally:
	print("End of program")
'''


#Reverse contents of a file
'''with open('f1.txt', 'r') as file:
    content = file.read()
reversed_content = content[::-1]
with open('f3.txt', 'w') as file:
    file.write(reversed_content)
'''

#copy contents of file
'''with open('f1.txt', 'r') as file:
   	content = file.read()
with  open('f3.txt', 'w') as file1:
	file1.write(content)'''
	


#read file count vowels
vowels = "aeiouAEIOU"
count = 0
v=0

with open('f3.txt', 'r') as file:
    content = file.read()
    for char in content:
        if char in vowels:
            count += 1
        else:
            v+=1

print(f"Number of vowels in the file: {count}")
print(f"Number of consonants in the file: {v}")

	




	

	




