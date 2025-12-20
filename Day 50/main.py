import os
import time
from selenium import webdriver
from selenium.common import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from random import randint

user_data_direction = os.path.join(os.getcwd(), "edge_profile")
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge_options.add_argument(f"--user-data-dir={user_data_direction}")

driver = webdriver.Edge(options=edge_options)
driver.get("https://tinder.com/")
wait = WebDriverWait(driver,2)
driver.refresh()


try:
    login_button = wait.until(ec.element_to_be_clickable(
        (By.XPATH, '//*[text()="Log in"]')
    ))
    login_button.click()
    # print("✅ Cookies declined!")
except TimeoutException:
    print("No login button found")
    # print("ℹ️ Cookie banner not found — skipping")


try:
    choose_facebook = wait.until(ec.element_to_be_clickable(
        (By.XPATH, '//button[contains(., "Log in with Facebook")]')
    ))
    choose_facebook.click()
except:
    print("No Facebook login found")

# Switch to the new pop-up window (for facebook)
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(2)
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys("jersey52@gmail.com")
password.send_keys("qwertyuiop[")
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

# Popups answers
def click_button(xpath, description):
    """try to click accept buttons"""
    try:
        btn = wait.until(ec.element_to_be_clickable(
            (By.XPATH, xpath)
        ))
        btn.click()
        print(f"✅ {description}")
        return True
    except:
        print(f"❌ {description} - not found")
        return False

click_button('//button[contains(., "Allow") or contains(., "ALLOW")]', "Location popup")
click_button('//button[contains(., "Not interested") or contains(., "NOT INTERESTED")]', "Notifications popup")
click_button('//button[contains(., "I accept") or contains(., "I ACCEPT")]', "Cookies popup")

for i in range(100):
    time.sleep(randint(1, 3))

    try:
        like_button = wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        ))
        like_button.click()
        print(f"💕 Like #{i + 1}")

    except ElementClickInterceptedException:
        # Match popup
        print("🎉 It's a Match!")
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            pass

    except TimeoutException:
        print("⏳ Loading... waiting 2 sec")
        time.sleep(2)

driver.quit()




