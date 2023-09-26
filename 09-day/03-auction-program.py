from art import logo


def highest_bidder(dictionary, name):
    max_bid = dictionary[name]
    for e in dictionary:
        if dictionary[e] > dictionary[name]:
            max_bid = dictionary[e]
            max_bidder = e
    print(f"max bid: ${max_bid} from {max_bidder}")


print(logo)
print("Welcome to the secret auction program.")

end_of_auction = False
auction_dict = {}

while not end_of_auction:
    name = input("what is your name?: ").lower()
    bid = int(input("What is your bid?: "))

    key_dict = name
    value_dict = bid

    auction_dict[name] = bid

    result = input("Are there any other bidders? Type Yes or No ").lower()

    if result == "no":
        highest_bidder(dictionary=auction_dict, name=name)
        print("End of auction!")
        end_of_auction = True


