"""what is perfect number?
A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself.
For example, the number 6 is a perfect number because its proper divisors are 1, 2, and 3, and their sum is 1 + 2 + 3 = 6."""

# Prompt the user to enter a number and convert it to an integer
num = int(input("Enter a number: "))

sum = 0 #initialize sum to 0

for i in range(1, num):# Loop through all numbers from 1 to num-1 

    if num % i == 0: #check if i is a divisor of num  , If it is, add it to sum
        sum += i

# Check if the sum of divisors is equal to the original number
if sum == num:  
    print("Perfect number")
else:
    print("Not a Perfect number")