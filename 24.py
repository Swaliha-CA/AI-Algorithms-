limit=int(input("Enter the limit:"))
a=0
b=1
if limit >= 1:
    print(a)
if limit >= 2:
    print(b)

count = 2  # Already printed the first two terms
while count < limit:
    next_term = a + b
    print(next_term)
    a = b
    b = next_term
    count += 1

	
