# The goal is to write a program that find out if a number is a prime number or not.

num = int(input("Please type in a number you want to check: "))


def prime(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It is a prime.")
    else:
        print("It is not a prime")

prime(number=num)
