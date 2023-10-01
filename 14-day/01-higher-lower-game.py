from art import logo, vs
from game_data import data
import random

# Display art.
print(logo)

# Generate a random account from the game data.
account_a = random.ranchoice(data)
account_b = random.ranchoice(data)
if account_a == account_b:
    account_b = random.choice(data)


def format_data(account):
    """"Format the account data into a printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"Compare A: {account_name}, a {account_descr}, from {account_country}")


print("Compare")
# Ask for a guess.

# Check if user is correct.
## Get follower count for each account
## Use if statement to check if user is correct.

# Give user feedback on their guess.

# Score keeping.

# Make the game repeatable.

# Making account at position B becomes the next account at position A.

# Clear the screen between rounds.
