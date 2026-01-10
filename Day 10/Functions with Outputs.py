def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())

format_name("nikITa", "lUtik")

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    print(f"{formated_f_name}\n{formated_l_name}")

format_name("nikITa", "lUtik")

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name}\n{formated_l_name}"

formated_string = format_name("nikITa", "lUtik")

print(formated_string)