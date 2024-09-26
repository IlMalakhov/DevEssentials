int_var = 10
float_var = 3.1415926
bool_var = True
user_int = int(input("Enter an integer: "))
user_float = float(input("Enter a float: "))

# Some conversions
float_int_var = float(int_var)         # Convert int to float
int_float_var = int(float_var)         # Convert float to int
str_to_int = int("123")               # Convert string to int
int_bool_var = int(bool_var)           # Convert bool to int (True = 1, False = 0)

# More calculations with conversions
complex_sum = float_int_var + user_float + int_float_var
converted_sum = int_bool_var + user_int + str_to_int

print("Complex sum: ", complex_sum)
print("Sum of converted string, input integer and bool: ", converted_sum)