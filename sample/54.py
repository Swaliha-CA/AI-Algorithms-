#count the frequency in string
'''s="hello"
freq={}
for char in s:
	freq[char]=s.count(char)
print(freq)'''


s="hello"
freq={}
for char in s:
	freq[char]=freq.get(char,0)+1
print(freq)


