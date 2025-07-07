mark = int(input("Enter the score (out of 100): "))

if mark >= 90:
    print("Grade A")
elif mark >= 75 and mark <= 89:
    print("Grade B")
elif mark >= 60 and mark <= 74:
    print("Grade C")
elif mark >= 40 and mark <= 59:
    print("Grade D")
else:
    print("FAIL")

