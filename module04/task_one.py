"""Use MyModule to collect numbers and report their extrema."""

import MyModule


numbers = MyModule.get_a_list_of_numbers()
smallest = MyModule.find_min(numbers)
largest = MyModule.find_max(numbers)

print(f"The list of numbers is: {numbers}")
print(f"The minimal number is: {smallest}")
print(f"The maximal number is: {largest}")