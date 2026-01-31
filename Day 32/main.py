##################### Hard Starting Project ######################
import random
import smtplib
import datetime as dt
import pandas
import os

my_gmail = "alesspy7@gmail.com"
my_pass = os.environ.get('my_pass')
my_yahoo = "lutik.nikita228@gmail.com"
now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=my_pass)
        connection.sendmail(from_addr=my_gmail,
                            to_addrs=birthday_person["email"],
                            msg="Subject")
