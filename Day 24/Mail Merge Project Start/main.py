PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", "r") as names_f:
    names = names_f.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_f:
    l_contents = letter_f.read()
    for name in names:
        new_name = name.strip()
        new_letter = l_contents.replace(PLACEHOLDER, new_name)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as letter_to_send:
            letter_to_send.write(new_letter)
