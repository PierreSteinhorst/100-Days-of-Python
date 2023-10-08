print("Welcome to the love calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

combinedString = name1 + name2
lowerCaseString = combinedString.lower()

capT = lowerCaseString.count("t")
capR = lowerCaseString.count("r")
capU = lowerCaseString.count("u")
capE = lowerCaseString.count("e")
capL = lowerCaseString.count("l")
capO = lowerCaseString.count("o")
capV = lowerCaseString.count("v")

sumTrue = str(capT + capR + capU + capE)
sumLove = str(capL + capO + capV + capE)
result = int(sumTrue + sumLove)

if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif 40 <= result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}")
