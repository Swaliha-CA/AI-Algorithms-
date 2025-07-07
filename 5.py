a=input("Enter a sentence:")
b=a.split()
count=0
c="python"
for i in b:
	for j in i:
		count+=1
print(count)

print(a.upper())
print(a.lower())

d=a.replace("","_")
print(d)

if  c in a:
	print("Python in sentence")
else:
	print("No python word")


