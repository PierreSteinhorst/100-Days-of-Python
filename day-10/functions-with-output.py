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
    if firstname == "" or lastname == "":
        return "You didn't provide valid inputs."
    cap_fname = firstname.title()
    cap_lname = lastname.title()
    return f"{cap_fname} {cap_lname}"


# formated_string = format_name("PieRRE", "maren")
# print(formated_string)

print(format_name(input("What is your firstname? "), input("What is your lastname? ")))
