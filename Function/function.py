"""
funtion() = fumction is a block of statement that returns a specific task. A idea is to put some commonly or repeatedly done task together and make a function so that instead of writing a same code again and again for different inputs, we can call the function 

it increases code reusability and readability

syntax:
def function_name(parameters):
    statement(s)
    return statement

types of function:
1. Built-in functions- standard functions that are available to use in python
2. User-defined functions- functions defined by the users according to their requirements


we can define a with def keyword . We can add any type of functionalities and properties in it as we require 

funtion() with parameters:
def function_name(parameters: data_type):
    statement(s)
    return statement


default arguments: a default argument is a argument that assumes a default value if a value is not provided in the function call for that argument. 

keyword arguments : a idea is to allow the caller to specify the argument name with the value so that caller does not need to remember the order of the arguments


"""
def firstfun():
    print("its my first function")

#driver code 
firstfun() #output: its my first function






#function with parameters
def add(num1:int,num2:int):
    num3 = num1+num2
    return num3

#driver code
num1 , num2 = 10, 990
ans = add(num1,num2)
print(f"addition of {num1} and {num2} is {ans}") #output: 1000







#funtion with default arguments
def default_argument(num1:int,num2:int=3565):
    print(f"num1 = {num1}")
    print(f"num2 = {num2}")

#driver code
default_argument(10) 






#function with keyword arguments
def keyword_argument(name:str,age:int):
    print(f"name = {name}")
    print(f"age = {age}")

#on below code order of the arguments are different but it will not affect the output because we are using keyword arguments

#driver code
keyword_argument(age=20,name="shubham") #output: name = shubham
                                        #        age = 20
keyword_argument(name="shubham",age=20) #output: name = shubham
                                        #        age = 20

