from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Edge Browser open after program finishes
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

# Create and configure the Edge webdriver
driver = webdriver.Edge(options=edge_options)

# Navigate to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# Option 2: driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)

# Find element by LINK TEXT
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
all_portals.click()

# Finding the "search" input by name
loop_button = driver.find_element(By.CLASS_NAME, value="mw-ui-icon-wikimedia-search")
loop_button.click()
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER) # Press ENTER

# Challenge 1
driver.get("https://secure-retreat-92358.herokuapp.com")

input_first_name = driver.find_element(By.NAME, value="fName")
input_last_name = driver.find_element(By.NAME, value="lName")
input_email = driver.find_element(By.NAME, value="email")
button = driver.find_element(By.CLASS_NAME, value="btn-block")

input_first_name.send_keys("Nikitos")
input_last_name.send_keys("Sankovich")
input_email.send_keys("nsankovchenko52@gmail.com")
button.click()
