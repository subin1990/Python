# importing module method 1

#import sub_file

#sub_file.sum_two_numbers()


# importing module method 2

import sub_file as s1

#print(s1.name)

# importing a specific function or variable from module

from sub_file import sum_two_numbers,name # we can add multiple thing support by coma
from sub_file import sum_two_numbers as s2 # this will also work
from sub_file import * # This will import all functions and variable from the module

sum_two_numbers()
print(name)
#print(help('modules'))
s2()
# in the case of two same names in imported module. the from import name should be like this subfile.name
name= 'Rajappan Thengummude'
import sub_file
print(sub_file.name)
