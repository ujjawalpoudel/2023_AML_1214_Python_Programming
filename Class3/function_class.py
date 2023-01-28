"""Class for function    """

# * Function without variable name
def withoutVarible():
    print("Without variable name")


# * Call function without variable name
withoutVarible()

# * Function with variable name, passing argument
def addition(a, b):
    print(f"Addition of {a} and {b} is {a + b}")


# * Call function with variable name
addition(1, 5)

# # * Function with variable name, input argument
# def sumNum():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print(f"Sum of {a} and {b} is {a + b}")

# # * Call function for addition
# sumNum()


# * Define function with variable name, passing argument
def helloWorldCanada():
    message = "Hello, Welcome to Canada!"
    print(message)


helloWorldCanada()

# * Global variable concept
first_num = 10
second_num = 20


# * Print global variable before function call
print(f"\nGLobal First number is {first_num}")
print(f"Gloabl Second number is {second_num}\n")


def addNumbers():
    first_num = 5
    second_num = 6
    print(f"Local First number is {first_num}")
    print(f"Local Second number is {second_num}\n")


# * Call function
addNumbers()

# * Print global variable after function call
print(f"GLobal First number is {first_num}")
print(f"Gloabl Second number is {second_num}\n")
