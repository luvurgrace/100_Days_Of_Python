import smtplib
import datetime as dt
from random import choice

my_gmail = "alesspy7@gmail.com"
my_pass = "hiden_pass"
my_yahoo = "lutik.nikita228@gmail.com"
now = dt.datetime.now()
today = now.weekday()

if today == 3: # if today is Thursday
    with open("quotes.txt") as f:
        all_quotes = f.readlines()
        quote = choice(all_quotes)

    # host: gmail - smtp.gmail.com, yahoo - smtp.mail.yahoo.com, hotmail - smtp.live.com
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls() # TLS - Transport Layer Security. It secures our connection by mail encryption
        connection.login(user=my_gmail, password=my_pass)
        connection.sendmail(from_addr=my_gmail,
                            to_addrs=my_yahoo,
                            msg=f"Subject: Thursday Motivation\n\n{quote}"
        )


# date_of_birth = dt.datetime(year = 2004, month = 9, day = 2, hour = 7, minute = 30)
# print(date_of_birth)
