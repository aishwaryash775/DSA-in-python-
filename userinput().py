#taking input from user
'''
# The input() function is used to take input from the user in Python. It reads a line of text from the user and returns it as a string. You can also provide a prompt message to guide the user on what to enter.
name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to Python programming.")
#output:
"
Enter your name: aishwarya premraj chavan  
Hello, aishwarya premraj chavan ! Welcome to Python programming.

age = input("Enter your age: ")
print("You are " + age + " years old.")
#output
Enter your age: 23
You are 23 years old.

'''
# lets create real  world calculators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# addition
add = a + b
#string concatenation to display the result str(a) converts the integer a to a string so that it can be concatenated with other strings in the print statement.

print("The sum of " + str(a) + " and " + str(b) + " is: " + str(add))
#
# subtraction
sub = a - b

print("The difference between " + str(a) + " and " + str(b) + " is: " + str(sub))
# multiplication
mul = a * b
print("The product of " + str(a) + " and " + str(b) + " is: " + str(mul))

# division
if b != 0:
    div = a / b
    print("The quotient of " + str(a) + " and " + str(b) + " is: " + str(div))  
else:
    print("Error: Division by zero is not allowed.")


# enter marks of 5 subjects and calculate the percentage
english_marks = int(input("Enter your English marks: "))
math_marks = int(input("Enter your Math marks: "))
science_marks = int(input("Enter your Science marks: "))
social_studies_marks = int(input("Enter your Social Studies marks: "))
hindi_marks = int(input("Enter your Hindi marks: "))
total_marks = english_marks + math_marks + science_marks + social_studies_marks + hindi_marks
percentage = (total_marks / 500) * 100
print("Your total marks are: " + str(total_marks))
print("Your percentage is: " + str(percentage) + "%")