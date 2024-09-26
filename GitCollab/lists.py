# Advanced data types
my_list = [1, 2, 3, "Python", 5.5]     # List
my_tuple = (10, 20, "tuple", 40.0)     # Tuples are immutable

user_to_list = input("Enter something to append to my_list: ")
my_list.append(user_to_list)
print("Updated list:", my_list) #add prompt to correctly and faster understand 

my_list.remove(user_to_list)
print("List after removal:", my_list)        # user_to_list is not in the list now

element = int(input("What index of tuple would you like to see? (0-3): "))
if 0 <= element <= 3:
    print("Index", element, "of my_tuple is", my_tuple[element])    # prints nth element of my_tuple
else: 
    print("Invalid! Please enter a number between 0 and 3")