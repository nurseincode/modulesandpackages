# import my_module # import full module

# print(my_module.greeting)
# print(my_module) # Prints the location on the module
# print(my_module.person)

# from my_module import person, foo # selective import
#foo(person)

import modules.my_module as my_module 
print(dir(my_module))
