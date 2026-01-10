from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Edge browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)



driver = webdriver.Edge(options=edge_options)
driver.get("https://www.python.org")

# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_fract = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"The price is £{price_whole}.{price_fract}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[1]/a') # like a file path
# print(bug_link.text)


# Challenge 1 - make a dictionary of Upcoming Events from Python.org

events_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div li a")
times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events = {}

for num in range(len(events_names)):
    events[num] ={
        "time": times[num].text,
        "name": events_names[num].text
    }

print(events)


driver.close() # Closes the current browser window/tab
driver.quit() #  Closes all browser windows and completely shuts down the WebDriver session


