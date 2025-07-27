'''fonction 1'''
def calculate_total(a, b):  # Parameters: a and b
   total = a * b           # Task: Addition
   return total            # Output: Sum of a and b

result = calculate_total(5, 4)  # Calling the function with inputs 5 and 7
print(result)  # Output: 12


'''fonction 2'''
def greet(name):
   return "Hello, " + name

result = greet("Alice")
print(result)  # Output: Hello, Alice


'''fonction 3'''
def multiply(a, b):
   """
   This function multiplies two numbers.
   Input: a (number), b (number)
   Output: Product of a and b
   """
   print(a * b)
multiply(2,6)


'''fonction 4'''
global_variable = "I'm global"
def example_function():
   local_variable = "I'm local"
   print(global_variable)  # Accessing global variable
   print(local_variable)   # Accessing local variable

example_function()
print(global_variable)  # Accessing global variable
print(local_variable)    # This will raise an error


'''fonction 5'''
def print_numbers(limit):
   for i in range(1, limit + 1):
       print(i)

print_numbers(5)  # Output: 1 2 3 4 5


'''fonction 6'''
def greet(name):
   return "Hello, " + name

for l in range(3):
   print(greet("paul"))


'''fonction 7'''
# Define an empty list as the initial data structure
my_list = []

# Function to add an element to the list
def add_element(data_structure, element):
   data_structure.append(element)

# Function to remove an element from the list
def remove_element(data_structure, element):
   if element in data_structure:
       data_structure.remove(element)
   else:
       print(f"{element} not found in the list.")

# Add elements to the list using the add_element function
add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)

# Print the current list
print("Current list:", my_list)

# Remove an element from the list using the remove_element function
remove_element(my_list, 17)
remove_element(my_list, 55)  # This will print a message since 55 is not in the list

# Print the updated list
print("Updated list:", my_list)



'''Exception '''

# using Try- except
try:
   # Attempting to divide 10 by 0
   result = 10 / 2
   print (result)
except ZeroDivisionError:
   # Handling the ZeroDivisionError and printing an error message
   print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")