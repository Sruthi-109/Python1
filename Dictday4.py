#1.Basic Input with Integer Conversion
#Take two numbers as input from the user, convert them to integers, and print their sum.

num1 = input("First number: ")
num2 = input("Second number: ")
num1 = int(num1)
num2 = int(num2)
sum = num1 + num2
print("The sum is:", sum)

#2.	Multiple Inputs with Space Separation
#Take two floating-point numbers as input in a single line separated by space and print their product.

num1, num2 = map(float, input("Enter two numbers separated by space: ").split())
product = num1 * num2
print("The product is:", product)

#3.	Expression Evaluation with eval()
#Take a mathematical expression from the user as input and print the evaluated result.

expression = input("Enter a mathematical expression: ")
result = eval(expression)
print("The result is:", result)

#4.	List Input using eval()
#Take a list as input using eval() and print the sum of its elements.

numbers = eval(input("Enter a list of numbers: "))
total = sum(numbers)
print("The sum of the list is:", total)

#5.	Boolean Type Conversion
#Take an input from the user, convert it to boolean, and print the result.

user_input = input("Enter a value: ")
bool_value = bool(user_input)
print("Boolean value is:", bool_value)

#6.	String to Float Conversion
#Take a floating-point number as string input, convert it to float, and print its square.

num_str = input("Enter a floating-point number: ")
num = float(num_str)
square = num ** 2
print("The square is:", square)

#7.	 Dictionary Input using eval()
#Take a dictionary as input using eval() and print its keys and values separately.

user_dict = eval(input("Enter a dictionary: "))
print("Keys:", list(user_dict.keys()))
print("Values:", list(user_dict.values()))

#8.	List of Integers from Space Separated Input
#Take a list of integers as input in a single line separated by space and print the maximum and minimum values.

numbers = list(map(int, input("Enter space-separated integers: ").split()))
maximum = max(numbers)
minimum = min(numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)

#9.	Mixed Type Literal Input with eval()
#Take any Python literal as input (string, list, tuple, int, etc.) using eval() and print its type.

user_input = eval(input("Enter any Python literal: "))
print("Type of input is:", type(user_input))

#10.	Combined Type Conversion
#Take two inputs, convert the first to integer and second to float, then print their sum.

num1 = input("Enter an integer: ")
num2 = input("Enter a floating-point number: ")
int_num = int(num1)
float_num = float(num2)
total = int_num + float_num
print("The sum is:", total)