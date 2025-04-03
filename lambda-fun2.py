#in this code we double number and triple number using lambda function

def myfunction(x):
    return lambda y: y * x

number = int(input("Enter a number: "))

double = myfunction(2)
print("The Double of given number is ", double(number))

triple = myfunction(3)
print("The Triple of given number is" , triple(number)) 

