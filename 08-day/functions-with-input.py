# def simple_greet():
#     print("Hello")
#     print(f"you are")
#     print("awesome!")
#
#
# simple_greet()
#
#
# def greet(name, age):
#     print("Hello " + name)
#     print(f"you are {age} years old.")
#     print("awesome!")
#
#
# greet("Pierre", 34)


# positional vs. keyword arguments
# Functions with more than 1 input
# -> positional arguments
# def greet_with(name, location):
#     print("Hello " + name + "!")
#     print("What is it like in " + location + "?")
#
#
# greet_with("Anna", "Berlin")
# greet_with("Berlin", "Anna")


# -> keyword arguments
def greet_with(name="Anna", location="Berlin"):
    print(f"Hello {name}!")
    print(f"What is it like in {location}")


greet_with(name="Anna", location="Berlin")
