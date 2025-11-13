# import requests

# # Download a web page
# response = requests.get("https://www.google.com/search?q=benguela")
# print(response.status_code)
name = "Alice"
age = 25
name = "Dave"

# vars cannot start with numbers
# vars cannot contain - 
# 2age = 20
# full-name = "John Doe"

# comment
"""
Multiline
Comments
With triple quotes
"""

# Data types
# number
total = 10 - 7
power = 10 ** 2

# print(power)

# String
string = "My name is Dave"
my_long_string = """
My name is Dave.
My last name is Ebbelazer
"""

# print(my_long_string)

first_name = "Dave"
last_name = "Ebbelaar"

full_name = first_name + " " + last_name
# print(full_name)

long_dash = "-" * 100
# print(long_dash)

# builting python functions
# print, len

len(long_dash)

# Boolean
# can be only True of False

is_logged_in = False
is_logged_in = True

age = 18
can_vote = age >= 18

# Logical operators
age = 25
has_licence = True
drunk = False

# AND - both conditions must be true
# OR - one of the conditions must be true
# Not - flips the value
# has_licence = not has_licence

can_drive = age >= 16 and has_licence and not drunk
# print(can_drive)

# String Manipulation
name = "Dave"
string = f"Hi there, my name is {name}!"
print(string)


