'''
def my_function(something):
    #Do something
    #Then do this
    #Finally ...
'''

'''
Functions with Outputs:
------------------------
def my_function():
    result = 3 * 2
    return result #This is the Output

output = my_function()
'''

# functions with outputs


def format_name(firstname, lastname):
    cap_fname = firstname.title()
    cap_lname = lastname.title()
    return f"{cap_fname} {cap_lname}"


formated_string = format_name("PieRRE", "maren")
print(formated_string)