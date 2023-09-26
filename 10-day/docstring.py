from pip._internal.resolution.resolvelib.base import format_name


def format_name(firstname, lastname):
    """Take a first and last name and format it to return the title case version of the name."""
    if firstname == "" or lastname == "":
        return "You didn't provide valid inputs."
    cap_fname = firstname.title()
    cap_lname = lastname.title()
    return f"{cap_fname} {cap_lname}"


formatted_name = format_name("PieRRE", "maren")

# Already used functions with outputs
length = len(formatted_name)

