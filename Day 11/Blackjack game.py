import random
from art import logo

def rand_card():
    """returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """returns Blackjack or sum of chosen cards (user's or computer's)"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw. "
    elif u_score == 0:
        return "You have Blackjack. You win! "
    elif c_score == 0:
        return "You lose. Your opponent has Blackjack. "
    elif u_score > 21:
        return "You went out. You lose. "
    elif c_score > 21:
        return "You win! Your opponent went out. "
    elif u_score > c_score:
        return "You win! You got the opponent. "
    else:
        return "You lose. Your opponent got you. "

def start_game():
    """start a new Blackjack game"""
    print(logo)
    user_cards = []
    comp_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(rand_card())
        comp_cards.append(rand_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score > 21 or user_score == 0 or comp_score == 0:
            game_over = True
        else:
            user_take_card = input("Type 'y' to take another card, or 'n' to pass: ")
            if user_take_card == "y":
                user_cards.append(rand_card())
            else:
                game_over = True
    while comp_score != 0 and comp_score < 17: # dealer always take under 17
        comp_cards.append(rand_card())
        comp_score = calculate_score(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n"*20)
    start_game()