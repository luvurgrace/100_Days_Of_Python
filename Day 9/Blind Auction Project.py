from art import logo

print("Welcome to the secret auction program!")
print(logo)

def find_highest_bidder(bids):
    winner = ''
    highest_bid = 0

    for person in bids:
        bid_amount = bids[person]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = person
            # max(bids, key=bids.get)
    print(f"The winner is {winner} with ${highest_bid} bid!")

bids = {}
auction_continue = True
while auction_continue:
    user_name = input("What is your name?\nMy name: ")
    user_bid = int(input("What is your bid?\nMy bid: "))
    another_user = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    bids[user_name] = user_bid
    if another_user == "yes":
        print("\n"*20)
    else:
        print("\n"*20)
        auction_continue = False
        find_highest_bidder(bids)
