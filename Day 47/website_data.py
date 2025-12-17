from bs4 import BeautifulSoup
import requests


class ReceiveDataFromAmazon:

    def __init__(self):
        self.URL = "https://www.amazon.co.uk/PlayStation-Sony-5-Digital-Edition/dp/B0FM3SBZK3/ref=sr_1_1?crid=12RY0TYX8TQEU&dib=eyJ2IjoiMSJ9.gQhZyRpGLafvyHBLaC0Pz5UZhFqUEOVAEHiEHCb0J64qWquwqd7TkFUe-L9hY2rdRMVZcT_KulnBun1LSOR-zqWK9DsgFapT0Wh5TVSm3R0QEEsRrFc7aflDwLyeg0tb0ZcMHXHkcNRyTuhQwNcvoIAf2p3QaanqczrWPq42uc95L_WXXfy5gYuXXmg0E4ZXYYh2Y-Sp5cRV1UcxJ95AvF0Ybfwc9MOc_9FxRbbpRc8.Z6OGsBeIYh-1mBMQuvoibE7o8Yet-COuXsErjsrWfB8&dib_tag=se&keywords=ps5&qid=1765976069&sprefix=ps5%2Caps%2C151&sr=8-1&th=1"
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

    def get_whole_price(self):
        price_whole=self.soup.find(class_="a-price-whole").getText()
        return price_whole

    def get_fract_price(self):
        price_fract=self.soup.find(class_="a-price-fraction").getText()
        return price_fract

    def get_product_name(self):
        p_name = ' '.join(self.soup.find("span", id="productTitle").getText().split())
        return p_name