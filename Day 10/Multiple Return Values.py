def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))

def can_buy_alcohol(age):
    # If the data type of the age input is not int, then exit.
    if type(age) != int:
        return

    if age >= 18:
        return "You are allowed to buy alcohol. "
    else:
        return "You are not allowed. "

i_allowed =  can_buy_alcohol(int(input("What is your age?\n")))

print(i_allowed)
