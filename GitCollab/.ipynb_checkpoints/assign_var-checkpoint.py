# Assigning an Integer, a Float, a Boolean and a String
int_var = 42
float_var = 3.1415926
bool_var = True
str_var = "Hi, "
user_int = int(input("Enter an integer: "))
user_float = float(input("Enter a float: "))
user_string = str(input("Enter your name: "))

# Do some calculations
sum_of_ints = int_var + user_int
product_of_floats = float_var * user_float
print(str_var + user_string)
print("Sum of int_var and your int:", sum_of_ints)
print("Sum of a boolean and your int:", bool_var + user_int)
print("Product of float_var and your float:", product_of_floats)

