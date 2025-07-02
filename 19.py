'''n=int(input("Enter the number:"))
rev=0
while n!=0:
  digit=n%10
  rev=rev*10+digit
  n//=10   # double // integer as output   and single / give float as output
print("Reversed number:",rev)
'''



n=input("Enter the number:")
print"reverse is",(n[::-1])
