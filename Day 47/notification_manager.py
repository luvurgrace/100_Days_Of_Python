import smtplib
import os
from dotenv import load_dotenv
from website_data import ReceiveDataFromAmazon

wd = ReceiveDataFromAmazon()
load_dotenv()
BUY_PRICE = 390

class NotificationManager:

    def __init__(self):
        self.email = os.environ["EMAIL_TO_SEND"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.connection = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"], 587)
        self.my_email = os.environ["MY_EMAIL_TO_RECEIVE"]

    def print(self):
        print(self.email)
        print(self.email_password)
        print(self.connection)

    def email_notify(self):
        if float(wd.get_whole_price()) < BUY_PRICE:
            with self.connection:
                self.connection.starttls()
                self.connection.login(self.email, self.email_password)
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=self.my_email,
                    msg=f"Subject:Amazon Price Alert!\n\n"
                        f"{wd.get_product_name()} is now £{wd.get_whole_price()}{wd.get_fract_price()}!\n\n"
                        f"Here is the link: https://www.amazon.co.uk/PlayStation-Sony-5-Digital-Edition/dp/B0FM3SBZK3/ref=sr_1_1?crid=12RY0TYX8TQEU&dib=eyJ2IjoiMSJ9.gQhZyRpGLafvyHBLaC0Pz5UZhFqUEOVAEHiEHCb0J64qWquwqd7TkFUe-L9hY2rdRMVZcT_KulnBun1LSOR-zqWK9DsgFapT0Wh5TVSm3R0QEEsRrFc7aflDwLyeg0tb0ZcMHXHkcNRyTuhQwNcvoIAf2p3QaanqczrWPq42uc95L_WXXfy5gYuXXmg0E4ZXYYh2Y-Sp5cRV1UcxJ95AvF0Ybfwc9MOc_9FxRbbpRc8.Z6OGsBeIYh-1mBMQuvoibE7o8Yet-COuXsErjsrWfB8&dib_tag=se&keywords=ps5&qid=1765976069&sprefix=ps5%2Caps%2C151&sr=8-1&th=1".encode('utf-8')
                )