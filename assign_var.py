# Assigning an Integer, a Float, a Boolean and a String
int_var = 42
float_var = 3.1415926
bool_var = True
#str_var = "Hi, "  #due to faster search of varieble in the output I would like to skip this one and just input greeting in the final output command
user_int = int(input("Enter an integer: "))
user_float = float(input("Enter a float: "))
user_string1 = str(input("Enter your name: "))
user_string2 = str(input("Enter your surname: ")) #just add one more var to observe more inf about user 

# Do some calculations
#sum_of_ints = int_var + user_int
#product_of_floats = float_var * user_float
print(f"Hi, {user_string1} {user_string2}") #there is my relocated greeting and also use advanced command f to provide cleaner and more readable code. Just found it doing my own codes, want do explain also that f-string in python lets you format data for printing using string templates
print("Sum of int_var and your int:", int_var + user_int) #make code smaller and faster to read
print("Sum of a boolean and your int:", bool_var + user_int)
print("Product of float_var and your float:", float_var * user_float) #also just put calculation with vars directly into output due to make code smaller 