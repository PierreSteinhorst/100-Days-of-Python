# Write your code below this line 👇
def prime_checker(number):
    """This method checks if a number is a prime number."""
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime.")
    else:
        print("It is not a prime.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
