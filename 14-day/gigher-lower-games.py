from game_data import data
from art import logo, vs
import random

# Chose a random entry from data to compare
## Create a random number for index
index_a = random.randint(0, len(data) - 1)
index_b = random.randint(0, len(data) - 1)
if index_a == index_b:
    equality = True
    while equality:
        index_b = random.randint(0, len(data) - 1)
        if index_a != index_b:
            equality = False

## Chose the equivalent entry of dictionary
random_dictionary_value_a = data[index_a]["follower_count"]
random_dictionary_value_b = data[index_b]["follower_count"]

print(logo)

print(f"Compare A: {data[index_a]['name']}, a {data[index_a]['description']}, from {data[index_a]['country']}.")
print(vs)
print(f"Compare B: {data[index_b]['name']}, a {data[index_b]['description']}, from {data[index_b]['country']}.")

decision = input("Who has more followers? Type 'A' or 'B': ").lower()

