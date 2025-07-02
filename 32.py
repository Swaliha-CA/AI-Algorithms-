'''def is_armstrong(n):
	digits=[int (d)  for d in str(n)]
	return n==sum(d**len(digits) for d in digits)
print(is_armstrong(153))'''

num = int(input("Enter a number: "))
original_num = num
num_digits = len(str(num))
sum_of_powers = 0

temp_num = num  # Use a temporary variable to manipulate for digit extraction
while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** num_digits
    temp_num //= 10

if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
