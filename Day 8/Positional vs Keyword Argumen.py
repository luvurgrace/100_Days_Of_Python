word_1 = "TRUE"
word_2 = "LOVE"

def calculate_love_score(name1, name2):
    name = (name1+name2).upper()
    num1 = num2 = 0
    for letter in word_1:
        if name.count(letter) > 0:
            num1 += name.count(letter)
    for letter in word_2:
        if name.count(letter) > 0:
            num2 += name.count(letter)
    love_score = "".join(map(str,[num1,num2]))
    print(love_score)

calculate_love_score("Barcelona", "Real Madrid")