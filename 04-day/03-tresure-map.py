# Your job is to write a program that allows you to mark a square on the map using a two-digit system.

# The first digit in the input will specify the column (the position on the horizontal axis).

# The second digit in the input will specify the row number (the position on the vertical axis).

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

positionColumn = int(position[0])
positionRow = int(position[1])

map[positionRow - 1][positionColumn - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")