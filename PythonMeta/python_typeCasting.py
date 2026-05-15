#Type Casting
#Two types of type casting in Python:
#1. Implicit Type Casting (Type Coercion) -> Python automatically converts one data type to another when performing operations that involve different data types. For example:
number_int = 42
number_float = 3.14
result = number_int + number_float  # Implicitly converts integer to float
print(result)  # Output: 45.14
#2. Explicit Type Casting (Type Conversion) -> You can explicitly convert a value from one data type to another using built-in functions. For example:
number_str = "42"
number_int = int(number_str)  # Explicitly converts string to integer
print(number_int)  # Output: 42
#Type casting, also known as type conversion, is the process of converting a value from one data type to another. In Python, you can use built-in functions to perform type casting. Here are some common type casting functions:
#1. int(): Converts a value to an integer.
#2. float(): Converts a value to a floating-point number.
#3. str(): Converts a value to a string.
#4. bool(): Converts a value to a boolean.
#5. list(): Converts a value to a list.
#6. tuple(): Converts a value to a tuple.
#7. set(): Converts a value to a set.
#8. dict(): Converts a value to a dictionary.
#9. frozenset(): Converts a value to a frozenset.
#10. complex(): Converts a value to a complex number.
#You can use these functions to perform type casting in Python. For example:
number_str = "42"
number_int = int(number_str)  # Convert string to integer
print(number_int)  # Output: 42

number_float = 3.14
number_int_from_float = int(number_float)  # Convert float to integer
print(number_int_from_float)  # Output: 3

number_int = 42
number_float = float(number_int)  # Convert integer to float
print(number_float)  # Output: 42.0 
is_student = True
is_student_str = str(is_student)  # Convert boolean to string
print(is_student_str)  # Output: 'True'
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # Convert list to tuple
print(my_tuple)  # Output: (1, 2, 3)
my_set = set(my_list)  # Convert list to set
print(my_set)  # Output: {1, 2, 3}
my_dict = dict(name="Alice", age=30)  # Convert keyword arguments to dictionary
print(my_dict)  # Output: {'name': 'Alice', 'age': 30}
my_frozenset = frozenset(my_list)  # Convert list to frozenset
print(my_frozenset)  # Output: frozenset({1, 2, 3})
number_complex = complex(number_int, number_float)  # Convert integer and float to complex number

print(number_complex)  # Output: (42+42j)   
#Note that when performing type casting, you should ensure that the value being converted is compatible with the target data type. For example, trying to convert a string that cannot be interpreted as a number to an integer will result in a ValueError. For example:
invalid_number_str = "abc"
try:
    invalid_number_int = int(invalid_number_str)
except ValueError:
    print("Error: Cannot convert string to integer.")  # Output: Error: Cannot convert string to integer.   
#Similarly, trying to convert a non-boolean value to a boolean will result in a ValueError. For example:
invalid_bool_str = "not a boolean"
try:
    invalid_bool = bool(invalid_bool_str)
except ValueError:
    print("Error: Cannot convert string to boolean.")  # Output: Error: Cannot convert string to boolean.       
#In summary, type casting is a useful technique in Python that allows you to convert values between different data types. It is important to use the appropriate type casting functions and ensure that the values being converted are compatible with the target data type to avoid errors.    
