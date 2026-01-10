from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
from dotenv import load_dotenv

load_dotenv()
PROMISED_DOWN = 80
PROMISED_UP = 8
X_EMAIL = os.environ.get("X_EMAIL")
X_PASS = os.environ.get("X_PASS")
X_URL = "https://x.com"
SPEEDTEST_URL="https://www.speedtest.net/ru"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.up = 0
        self.down = 0
        user_data_direction = os.path.join(os.getcwd(), "edge_profile")
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option("detach", True)
        edge_options.add_argument(f"--user-data-dir={user_data_direction}")
        self.driver = webdriver.Edge(options=edge_options)
        self.wait = WebDriverWait(self.driver, 3)
        self.main_window_handle = None
        self.new_window_handle = None

    def get_internet_speed(self, URL):
        self.driver.get(URL)
        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".js-start-test.test-mode-multi"))).click()
        sleep(45)
        download_mbps = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed"))).text
        upload_mpbs = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".result-data-large.number.result-data-value.upload-speed"))).text
        print(f"down: {download_mbps}")
        print(f"up: {upload_mpbs}")

        # base_window = self.driver.window_handles[0]
        # fb_login_window = self.driver.window_handles[1]
        # self.driver.switch_to.window(fb_login_window)

    def tweet_at_provider(self, URL):
        self.driver.get(URL)
        sleep(3)

        self.main_window_handle = self.driver.current_window_handle

        self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/button'))).click()

        self.switch_to_new_window()

        username_input = self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="account_name_text_field"]')))
        username_input.clear()
        username_input.send_keys(X_EMAIL)
        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="sign-in"]'))).click()
        password_input = self.wait.until(ec.presence_of_element_located((By.ID, "password_text_field")))
        password_input.clear()
        password_input.send_keys(X_PASS)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="sign-in"]'))).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="1766328055442-0"]/div/div/button[1]'))).click()
        self.wait.until(ec.presence_of_element_located(
            (By.CLASS_NAME, 'button.button-primary.last.nav-action.pull-right.weight-medium')))
        finish_button = self.driver.find_element(By.CLASS_NAME,
                                                 value='button.button-primary.last.nav-action.pull-right.weight-medium')
        finish_button.click()
        self.switch_to_main_page()

        self.wait.until(ec.presence_of_element_located((By.XPATH,
                                                        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')))
        input_tweet = self.driver.find_element(By.XPATH,
                                               value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        input_tweet.send_keys(
            f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        next_button = self.driver.find_element(By.XPATH,
                                               value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        next_button.click()


    def switch_to_new_window(self):
        for handle in self.driver.window_handles:
            if handle != self.main_window_handle:
                self.new_window_handle = handle
                break
        self.driver.switch_to.window(self.new_window_handle)

    def switch_to_main_page(self):
        self.driver.switch_to.window(self.main_window_handle)

driver_speed = InternetSpeedTwitterBot()
driver_speed.get_internet_speed(SPEEDTEST_URL)
driver_speed.tweet_at_provider(X_URL)