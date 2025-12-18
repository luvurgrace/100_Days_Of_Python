from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from time import sleep, time

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=edge_options)
driver.get("https://ozh.github.io/cookieclicker")
sleep(3)

driver.find_element(By.ID, value="langSelect-EN").click()
sleep(2)
driver.find_element(By.CLASS_NAME, value="cc_btn_accept_all").click()
sleep(1)

cookie = driver.find_element(By.ID, value="bigCookie")

timeout = time() + 5
game_time = time() + 60 * 5  # 5 mins

while True:
    # Cookie clicks
    try:
        cookie.click()
    except StaleElementReferenceException:
        cookie = driver.find_element(By.ID, value="bigCookie")
        cookie.click()

    # Catch the deer
    shimmers = driver.find_elements(By.CSS_SELECTOR, ".shimmer")
    for shimmer in shimmers:
        try:
            shimmer.click()
            print("✨ Bonus Received!")
        except:
            pass

    # Purchases every 5 seconds
    if time() > timeout:
        # Upgrades
        try:
            driver.find_element(By.ID, value="upgrade0").click()
        except:
            pass

        # Picks most valuable product
        items_to_buy = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
        if items_to_buy:
            try:
                items_to_buy[-1].click()
            except:
                pass

        timeout = time() + 5

    # Game over
    if time() > game_time:
        try:
            cps = driver.find_element(By.ID, "cookiesPerSecond").text
            cookies_per_second = cps.split()[2]
            print(f"🍪 Final cookies per second: {cookies_per_second}")
        except:
            print("Could not get final cookie count")
        break

print("Game over!")
driver.quit()