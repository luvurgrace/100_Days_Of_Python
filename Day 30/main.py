# File not found
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existent_key"]

# IndexError
# fruit_list = ["Apple","Banana","Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# try: # executing smth that might cause an exception (for times the code may not work)
#     file = open("a_file.txt", "r")
#     a_dict = {"key": 1}
#     print(a_dict["key"])
# except FileNotFoundError: # do this if there was an exception (except: will ignore all errors)
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else: # do this if there were no exceptions
#     print(file.read())
# finally: # do this no matter what happens
#     raise KeyError("HMMM") # raise our own exceptions

# height=float(input("Height:"))
# weight=int(input("Weight:"))
#
# if height>3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight/height ** 2
# print(bmi)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes += post['Likes']
        except KeyError:
            total_likes += 0


    return total_likes


print(count_likes(facebook_posts))

