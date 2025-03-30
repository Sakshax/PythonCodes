def is_palindrome_number(num):#defining function 
    return str(num) == str(num)[::-1] # Check if the number is equal to its reverse

#driver code
num = int(input("Enter a number: "))
if is_palindrome_number(num):
    print("Palindrome number")
else:
    print("Not a Palindrome number")
