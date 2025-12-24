import os
from dotenv import load_dotenv
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()

class DataManager:

    def __init__(self):
        self.URL = os.getenv("URL")
        self.HEADERS = {
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
             "Accept-Encoding": "gzip, deflate, br, zstd",
             "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
             "Dnt": "1",
             "Priority": "u=1",
             "Sec-Fetch-Dest": "document",
             "Sec-Fetch-Mode": "navigate",
             "Sec-Fetch-Site": "none",
             "Sec-Fetch-User": "?1",
             "Sec-Gpc": "1",
             "Upgrade-Insecure-Requests": "1",
             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0"
        }
        self.response = requests.get(self.URL, headers = self.HEADERS)
        self.response.raise_for_status()
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def get_house_link(self, house):
        self.link = house.select_one("a").get_attribute_list("href")[0]
        return self.link


    def get_house_price(self, house):
        self.price = house.select_one('span[data-test="property-card-price"]').text.replace("/mo", "").split("+")[0].strip()
        return self.price


    def get_house_address(self, house):
        self.address = " ".join(house.select_one('address[data-test="property-card-addr"]').text.replace("|", "").split())
        return self.address

    def make_full_house_data(self):
        self.houses = []
        for house in self.soup.select('ul li[class^="ListItem-c11n"]'):
            self.house = {
                "address": self.get_house_address(house),
                "price": self.get_house_price(house),
                "link": self.get_house_link(house)
            }
            self.houses.append(self.house)


class DataFilling:

    def __init__(self):
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(edge_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.POLL_URL = os.getenv("POLL_URL")

    def fill_the_sheet(self, house):
        print(house)

        self.driver.get(self.POLL_URL)
        self.wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        address_input = self.driver.find_element(By.XPATH,
                                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input = self.driver.find_element(By.XPATH,
                                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input = self.driver.find_element(By.XPATH,
                                              '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(house["address"])
        price_input.send_keys(house["price"])
        link_input.send_keys(house["link"])
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit_button.click()
        sleep(2)


dm = DataManager()
dm.make_full_house_data()

df = DataFilling()
for house in dm.houses:
    df.fill_the_sheet(house)


