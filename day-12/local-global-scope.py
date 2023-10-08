######################## Scope ########################

# Modify Global Scope
# enemies = 1
#
#
# def increase_enemies():
#
#     print(f"Enemies inside function: {enemies}")
#     return enemies +1
#
# enemies = increase_enemies()
# increase_enemies()
# print(f"Enemies outside function: {enemies}")

# Local Scope


# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)


# drink_potion()
# print(potion_strength)

# Global Scope

# player_health = 10
#
#
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#     drink_potion()
#
#
# print(player_health)


# There is no block scope

# game_level = 3
# enemies = ["Skeleton", "Zombie","Alien"]
#
#
# def create_enemy():
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)

# Global Constants

PI = 3.14159
URL = "https://www.google.com"



