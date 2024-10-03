import smallest_module
import int_lists_module

file = open('result.txt', 'a')
file.write(str(smallest_module.find_two_smallest(int_lists_module.int_list1)) + '\n')
file.write(str(smallest_module.find_two_smallest(int_lists_module.int_list2)) + '\n')
file.close()