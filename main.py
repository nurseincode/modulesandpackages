# import my_module # import full module

# print(my_module.greeting)
# print(my_module) # Prints the location on the module
# print(my_module.person)

# from my_module import person, foo # selective import
#foo(person)

# import modules.my_module as my_module # as keyword creates an alias for my-module
# print(dir(my_module))

from color50 import rgb, constants

my_color = rgb(128, 0, 128)
# print(my_color + "Hello, World!" + constants.RESET) # Sets terminal color to purple
print(constants.YELLOW + "Hello World!" + constants.RESET) # to yellow
