from game_data import data
from art import logo, vs
import random

print(logo)


def random_index(src_list):
    index = random.randint(0, len(src_list) - 1)
    return index


def value_of_follower(index, src_list):
    value = src_list[index]["follower_count"]
    return value


def compare_values(first_value, second_value):
    decision = input("Who has more followers? Type 'A' or 'B': ").lower()
    score = 0
    if decision == "a":
        if first_value > second_value:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
    elif decision == "b":
        if second_value > first_value:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")


index_a = random_index(data)
value_a = value_of_follower(index_a, data)
index_b = random_index(data)
value_b = value_of_follower(index_b, data)

print(
    f"Compare A: {data[index_a]['name']}, a {data[index_a]['description']}, from {data[index_a]['country']}: Follower {value_a}.")
print(vs)
print(
    f"Compare A: {data[index_b]['name']}, a {data[index_b]['description']}, from {data[index_b]['country']}: Follower {value_b}.")

compare_values(value_a, value_b)

# print(random_index(data))
# print(random_index(data))
# print(value_of_follower(random_index(data), data))
# print(value_of_follower(random_index(data), data))

# ## Chose the equivalent entry of dictionary
# random_dictionary_value_a = data[index_a]["follower_count"]
# random_dictionary_value_b = data[index_b]["follower_count"]
