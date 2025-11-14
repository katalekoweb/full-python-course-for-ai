def greeting (): # lower case letters with underscore
    print("GoddBye!")

def send_email():
    pass

def validate_pasword():
    pass

def check_weather():
    temperature = 30
    if temperature > 25:
        print("It's hot!")
    else:
        print("Thats a good clime")

# params
def greet (first_name, last_name="Kataleko"):
    print(f"Hello {first_name} {last_name}")
    
global_discount = 20
def calculate_price (price, tax_rate, discount):
    
    # Calculation
    tax = price * tax_rate
    final_price = price + tax - global_discount
    
    # Print the final price
    print(f"Total: $ {final_price}")
    
# Return
def sum (a, b):
    return a + b

def calculate_area (width, height):
    return width * height

# Multple returns
def simple_function () :
    numbers = [1,2,3,4,5]
    first_number = numbers[0]
    last_number = numbers[-1]
    return first_number, last_number

result = sum(10, 30)

# greeting()
# greeting()
# greeting()
# check_weather()
# greet("Julian", "Kataleko")
# greet(first_name="Mariana", last_name="Kataleko")
# greet(first_name="Florinda")
# greet(first_name="Belisa")

# calculate_price(price=100,tax_rate=0.14, discount=0.00)

first_number, last_number = simple_function()
print(simple_function())
print(first_number)