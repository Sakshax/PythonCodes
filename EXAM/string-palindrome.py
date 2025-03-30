def is_palindrome(string):#defining function
    return string == string[::-1]#check if the string is equal to its reverse
#driver code
string = input("Enter a string: ")
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a Palindrome")
