#Naming Conventions in Python
#camel case
myVariable = 10
print(myVariable)
#snake case
my_variable = 20
print(my_variable)
#pascal case
MyVariable = 30
print(MyVariable)
#kebab case is not allowed in Python variable names, as it uses hyphens which are not valid characters for variable names.  
#kebab-case = 40 # This will cause a syntax error in Python.

#Variable naming rules in Python:
#1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
#2. Variable names can only contain letters, numbers, and underscores.  
#3. Variable names are case-sensitive (e.g., myVariable and myvariable are different variables).    
#4. Variable names cannot be a reserved keyword in Python (e.g., if, else, while, for, etc.).   
#5. Variable names should not start with a number (e.g., 1variable is invalid).
#6. Variable names should be descriptive and meaningful to enhance code readability (e.g., age instead of a).   

#Example of valid variable names:
age = 25
first_name = "John"
_last_name = "Doe"
#Example of invalid variable names:
#1variable = 10 # Invalid: starts with a number
#my-variable = 20 # Invalid: contains a hyphen
#class = "Python" # Invalid: 'class' is a reserved keyword

#Best practices for variable naming:
#1. Use descriptive names that clearly indicate the purpose of the variable (e.g., total_price instead of tp).
#2. Use lowercase letters and underscores for variable names (snake_case) to improve readability.   
#3. Avoid using single-character variable names except for loop counters (e.g., i, j, k).
#4. Be consistent with your naming conventions throughout your codebase to enhance readability and maintainability. 

#Variable assignment and usage:
x = 10  
y = 20
z = x + y
print("The sum of x and y is:", z)

#Variable reassignment:
x = 15  # Reassigning x to a new value
print("The new value of x is:", x)  

#Variable types:
name = "Alice"  # String
age = 25  # Integer
height = 5.9  # Float
is_student = True  # Boolean
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

#Variable scope:
def my_function():
    local_variable = "I am local to this function"
    print(local_variable)

my_function() 
# print(local_variable)  # This will cause an error because local_variable is not accessible outside the function.  

#Global variable example:
global_variable = "I am a global variable"
print("Global variable:", global_variable)

#Using global variable inside a function:
def access_global_variable():
    print("Accessing global variable inside function:", global_variable)

access_global_variable()

#Modifying global variable inside a function:
def modify_global_variable():
    global global_variable  # Declare that we want to use the global variable
    global_variable = "I have been modified inside the function"
modify_global_variable()
print("Global variable after modification:", global_variable)

#Constants in Python:
#In Python, there is no built-in constant type, but by convention, we use uppercase letters to indicate that a variable is intended to be a constant (i.e., its value should not be changed).
PI = 3.14159
print("Value of PI:", PI)

#While we can technically reassign a new value to PI, it is generally discouraged as it goes against the convention of using uppercase letters for constants.
#PI = 3.14  # This is technically allowed but not recommended as it can lead to confusion and bugs in the code. 

#initializing multiple variables in one line:
a, b, c = 1, 2, 3
print("Values of a, b, c:", a, b, c)

d= e = f = 0  # All three variables are initialized to 0
print("Values of d, e, f:", d, e, f)

