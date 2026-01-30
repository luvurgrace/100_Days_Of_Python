import random
from art import logo
from art import vs
from game_data import data



def random_dictionary(list):
    """random dictionary is chosen"""
    return random.choice(list)

def get_name(dictionary):
    """returns a name from chosen dictionary"""
    name = dictionary["name"]
    return name

def get_followers(dictionary):
    """returns followers count from chosen dictionary"""
    follower_count = dictionary["follower_count"]
    return follower_count

def get_description(dictionary):
    """returns description from chosen dictionary"""
    description = dictionary["description"]
    return description

def get_country(dictionary):
    """returns a country from chosen dictionary"""
    country = dictionary["country"]
    return country

def format_data(dictionary, letter):
    name = get_name(dictionary)
    description = get_description(dictionary)
    country = get_country(dictionary)
    return f"Compare {letter}: {name}, a {description}, from {country}. "

game_over = False
score = 0
dict_A = random_dictionary(data)
dict_B = dict_A
print(logo)

# start a game
while not game_over:
    while dict_B == dict_A:
        dict_B = random_dictionary(data)
    print(format_data(dict_A, "A"))
    print(vs)
    print(format_data(dict_B, "B"))
    answer = input("Who has more followers? Type 'A' or 'B': ").upper()
    if answer == "A":
        if get_followers(dict_A) > get_followers(dict_B):
            score += 1
            print('\n' * 20)
            print(logo)
            print(f"You're right! Current score: {score}.")
            dict_B = random_dictionary(data)
            while dict_B == dict_A:
                dict_B = random_dictionary(data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_over = True
    else:
        if get_followers(dict_A) < get_followers(dict_B):
            print('\n'*20)
            print(logo)
            score += 1
            print(f"You're right! Current score: {score}.")
            dict_A = dict_B
            dict_B = random_dictionary(data)
            while dict_B == dict_A:
                dict_B = random_dictionary(data)
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_over = True
