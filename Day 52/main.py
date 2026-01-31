import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()
SIMILAR_ACCOUNT = "neymarjr"
USERNAME = os.getenv("INSTUSERNAME")
PASSWORD = os.getenv("PASSWORD")
URL = "https://www.instagram.com"

class InstaFollower:

    def __init__(self):
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option("detach", True)
        user_data_dir = os.path.join(os.getcwd(), "edge_profile")
        edge_options.add_argument(f"--user-data-dir={user_data_dir}")
        self.driver = webdriver.Edge(edge_options)
        self.wait = WebDriverWait(self.driver, 3)

    def login(self):
        try:
            self.driver.get(f"{URL}/accounts/login/")
            username_input = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))
            username_input.send_keys(USERNAME)
            pass_input = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
            pass_input.send_keys(PASSWORD)
            self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button'))).click()
        except:
            print("No login")
        try:
            not_now_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Click me')]")))
            not_now_btn.click()
        except:
            print("No popup appeared.")

    def find_followers(self):
        self.driver.get(f"{URL}/{SIMILAR_ACCOUNT}")
        followers_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, f"//a[contains(@href, '/{SIMILAR_ACCOUNT}/followers/')]"))
        )
        followers_button.click()

    def follow(self):
        time.sleep(3)

        buttons = self.driver.find_elements(
            By.XPATH, '//button[contains(., "Follow")]'
        )

        # Fallback: search in dialog
        if not buttons:
            all_buttons = self.driver.find_elements(
                By.CSS_SELECTOR, 'div[role="dialog"] button'
            )
            buttons = [b for b in all_buttons if "Follow" in b.text]

        print(f"Found {len(buttons)} buttons")

        for btn in buttons:
            try:
                btn.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                try:
                    self.driver.find_element(
                        By.XPATH, '//button[contains(., "Cancel")]'
                    ).click()
                except:
                    pass

inf = InstaFollower()
inf.login()
inf.find_followers()
inf.follow()