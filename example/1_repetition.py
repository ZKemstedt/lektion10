'''
When we import, define function and define variables
we bind a name that refers to a Object.

Until now we have used
- Built-in functions: i.e slice, chr, str, range, int
    see [https://docs.python.org/3/library/functions.html#built-in-functions]

- Build-in constants i.e False, True, None
    see: [https://docs.python.org/3/library/constants.html#built-in-consts]

- Functions definitions i.e def a_func()
    see: [https://docs.python.org/3/reference/compound_stmts.html#function-definitions]

'''
# assign a list to a variable
a_list = [5, 3, 4, 1, 2]

# A variable
a_string = "a string value"

# using built-in function slice and assign it
a_sliced_string = a_string[0:9]


# defining a function
def a_func(attribute):
    if(attribute):
        return True


'''
- The Callable types can be used with call operation "()" i.e func_name()
    see [https://docs.python.org/3/reference/expressions.html#calls]

    - User-defined functions
    - Built-in functions i.e len()
    - Built-in methods i.e when you use a_list.append() or a_list.sort()
'''
# Call a built-in function
len(a_list)

# Call a user-defined function
a_func(123)

# Call a Built-in method
a_list.sort()

'''
We can use type() to investigate their type
    see [https://docs.python.org/3/library/functions.html#type]
'''


'''
The type hierarchy list all pre defined types:
see [https://docs.python.org/3/reference/datamodel.html#the-standard-type-hierarchy]

Type hierarchy - Callable type
    - The Callable types can be used with call operation "()" i.e func_name()
    see [https://docs.python.org/3/reference/expressions.html#calls]

    - User-defined functions
    - Built-in functions i.e len()
    - Built-in methods i.e when you use a_list.append() or a_list.sort()
'''
