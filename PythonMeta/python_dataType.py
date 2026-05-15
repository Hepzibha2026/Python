#Python Data Types
#Python has several built-in data types that are used to store different types of data. Here are some of the most commonly used data types in Python:   
#1. Numeric Types:
#   - int: Represents integer values (e.g., 1, 42, -100).
#   - float: Represents floating-point numbers (e.g., 3.14, -0.001).
#   - complex: Represents complex numbers (e.g., 2 + 3j).
#2. Sequence Types:
#   - list: An ordered, mutable collection of items (e.g., [1, 2, 3], ['a', 'b', 'c']).
#   - tuple: An ordered, immutable collection of items (e.g., (1, 2, 3), ('a', 'b', 'c')).
#   - range: Represents a sequence of numbers (e.g., range(0, 10)).
#3. Text Type:
#   - str: Represents a sequence of characters (e.g., "Hello, World!").
#4. Mapping Type:
#   - dict: Represents a collection of key-value pairs (e.g., {'name': 'Alice', 'age': 30}).
#5. Set Types:
#   - set: An unordered collection of unique items (e.g., {1, 2, 3}, {'a', 'b', 'c'}).
#   - frozenset: An immutable version of a set (e.g., frozenset({1, 2, 3})).
#6. Boolean Type:
#   - bool: Represents a boolean value, which can be either True or False.
#7. None Type:
#   - None: Represents the absence of a value or a null value.
#You can use the built-in type() function to check the data type of a variable or value. For example:
x = 10
print(type(x))  # Output: <class 'int'>
y = 3.14
print(type(y))  # Output: <class 'float'>
name = "Alice"
print(type(name))  # Output: <class 'str'>
my_list = [1, 2, 3]
print(type(my_list))  # Output: <class 'list'>
my_dict = {'name': 'Alice', 'age': 30}
print(type(my_dict))  # Output: <class 'dict'>
my_set = {1, 2, 3}
print(type(my_set))  # Output: <class 'set'>
my_frozenset = frozenset({1, 2, 3})
print(type(my_frozenset))  # Output: <class 'frozenset'>    
is_student = True
print(type(is_student))  # Output: <class 'bool'>
none_value = None
print(type(none_value))  # Output: <class 'NoneType'>
#Data types in Python
#1. Numeric Types:
#2. Sequence Types:
#3. Dictionary Type:
#4. Boolean Type:
#5. Set Types:

#Numeric Types:
#1. Integer
#2. Float
#3. Complex Number

#Sequence Types:
#1. String
#2. List
#3. Tuples

#Dictionary Type:
#1. Dictionary  - key value pair
#Boolean Type:
#1. Boolean
#Set Types:
#1. Set
#2. Frozen Set  

#strings in Python are immutable, which means that once a string is created, it cannot be modified. However, you can create new strings by concatenating existing strings or using string formatting. For example:
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"  # Concatenation
print(message)  # Output: Hello, Alice!
formatted_message = f"{greeting}, {name}!"  # String formatting using f-string
print(formatted_message)  # Output: Hello, Alice!
#You can also use the str() function to convert other data types to strings. For example:
number = 42
number_str = str(number)  # Convert integer to string
print(number_str)  # Output: '42'
pi = 3.14
pi_str = str(pi)  # Convert float to string
print(pi_str)  # Output: '3.14'

#multi-line strings in Python can be created using triple quotes (''' or """). They are often used for docstrings, which are multi-line comments that describe the purpose of a function, class, or module. For example:
def my_function():
    """This is a docstring that describes the purpose of the function."""
    print("Hello, World!")
my_function()  # Output: Hello, World!
#multi-line strings using \ for combining lines:
multi_line_string = "This is a multi-line string that " \
                    "is created using the backslash character " \
                    "to combine multiple lines into one string."
print(multi_line_string)  # Output: This is a multi-line string that is created using the backslash character to combine multiple lines into one string.    

#Indentation in Python is crucial as it defines the scope of loops, functions, and other code blocks. Proper indentation is necessary for the code to run correctly. For example:
def my_function():
    print("This is inside the function.")
    if True:
        print("This is inside the if statement.")
    print("This is still inside the function.") 
my_function()   

