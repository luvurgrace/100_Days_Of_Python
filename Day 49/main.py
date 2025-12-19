import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
from dotenv import load_dotenv

# Data for registration
load_dotenv()
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASS = os.environ.get("MY_PASSWORD")
MY_NAME = "Nikita"

# Booking summary start data
BOOKED = 0
WAITLISTS = 0
ALREADY = 0
TOTAL = 0
processed_classes = []

def retry(func, retries=7, description=None):
    """Retry function - till it gets True"""
    for i in range(retries):
        print(f"🔄 Trying {description}. Attempt: {i + 1}/{retries}")
        try:
            result = func()
            if result:  # If success - print
                print(f"✅ {description} - Success!")
                return True
            else:
                print(f"❌ Attempt {i + 1} returned False")
        except Exception as e:
            print(f"❌ Attempt {i + 1} error: {e}")

        time.sleep(1)  # Pause between attempts

    print(f"❌ All {retries} attempts failed {description}")
    return False

user_data_dir = os.path.join(os.getcwd(), "edge_profile")

# Edge Settings
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
edge_options.add_argument(f"--user-data-dir={user_data_dir}")

# Launch
driver = webdriver.Edge(options=edge_options)
driver.get("https://appbrewery.github.io/gym")

# Timeout
wait = WebDriverWait(driver, 2)

def login():
    try:
        login_button = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        #  Email and password are being provided
        email_input = wait.until(ec.element_to_be_clickable((By.ID, "email-input")))
        email_input.clear()
        email_input.send_keys(MY_EMAIL)
        pass_input = wait.until(ec.element_to_be_clickable((By.ID, "password-input")))
        pass_input.clear()
        pass_input.send_keys(MY_PASS)
        # Submit login data provided
        driver.find_element(By.ID, "submit-button").click()
        wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
        return True
    except:
        return False

def booking():
    global TOTAL, BOOKED, WAITLISTS, ALREADY
    try:
        # Tuesday/Thursday 6 pm bookings
        events = driver.find_elements(By.CSS_SELECTOR, "div[id^='day-group']")
        for event in events:
            event_day = event.find_element(By.TAG_NAME, "h2").text

            if "Tue" in event_day or "Thu" in event_day:
                times = event.find_elements(By.CSS_SELECTOR, "p[id^='class-time-']")

                for time in times:
                    if "6:00 PM" in time.text:
                        time_index = times.index(time)
                        event_name = event.find_elements(By.CSS_SELECTOR, "h3[id^='class-name-']")[time_index].text
                        booking_button = event.find_elements(By.CSS_SELECTOR, "button[id^='book-button-']")[time_index]
                        booking_data = f"{event_name} is on {event_day}!"
                        type_ = booking_button.text
                        if type_ == "Book Class":
                            booking_button.click()
                            print(f"\n🤗 Booked: {booking_data}")
                            BOOKED += 1
                            TOTAL += 1
                            processed_classes.append(f"[New Booking] {booking_data}")
                        elif type_ == "Join Waitlist":
                            booking_button.click()
                            print(f"\n🤗 Joined waitlist for: {booking_data}")
                            WAITLISTS += 1
                            TOTAL += 1
                            processed_classes.append(f"[New Waitlist] {booking_data}")
                        elif type_ == "Booked":
                            print(f"\n🤗 Already booked: {booking_data}")
                            ALREADY += 1
                            TOTAL += 1
                            processed_classes.append(f"[Booked] {booking_data}")
                        elif type_ == "Waitlisted":
                            print(f"\n🤗 Already on waitlist: {booking_data}")
                            ALREADY += 1
                            TOTAL += 1
                            processed_classes.append(f"[Waitlisted] {booking_data}")
                        else:
                            print("\nNo booking found")
        return True
    except:
        return False

def check_bookings():
    try:
        print(f"""
--- BOOKING SUMMARY ---
Classes booked: {BOOKED}
Waitlists joined: {WAITLISTS}
Already booked/waitlisted: {ALREADY}
Total Tuesday/Thursday 6pm classes processed: {TOTAL}
""")

        print("\n--- DETAILED CLASS LIST ---")
        for class_detail in processed_classes:
            print(f"  • {class_detail}")

        booking_page_link = driver.find_element(By.ID, "my-bookings-link")
        booking_page_link.click()

        confirmed_bookings = driver.find_elements(By.CSS_SELECTOR, '[data-booking-status="confirmed"]')
        confirmed_waitlists = driver.find_elements(By.CSS_SELECTOR, '[data-booking-status="waitlisted"]')
        CONFIRMED = len(confirmed_bookings)+len(confirmed_waitlists)

        if TOTAL>0:
            print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
            for conf_booking in confirmed_bookings:
                print(f" ✓ Verified: {conf_booking.find_element(By.TAG_NAME, "h3").text}")
            for conf_waitlist in confirmed_waitlists:
                print(f" ✓ Verified: {conf_waitlist.find_element(By.TAG_NAME, "h3").text}")

            print(f"""\n
--- VERIFICATION RESULT ---
Expected: {TOTAL} bookings
Found: {CONFIRMED} bookings""")
        if CONFIRMED == TOTAL:
            print("\n✅ SUCCESS: All bookings verified!")
        else:
            print(f"\n❌ MISMATCH: Missing {CONFIRMED-TOTAL} bookings")
        return True
    except:
        return False

def register():
    if driver.find_element(By.CSS_SELECTOR, '[id="error-message"]'):
        driver.find_element(By.CSS_SELECTOR, 'button[id="toggle-login-register"]').click()
        name_input = wait.until(ec.element_to_be_clickable((By.ID, "name-input")))
        name_input.clear()
        name_input.send_keys(MY_NAME)
        driver.find_element(By.ID, "submit-button").click()

login_success = retry(login, 7, "to login")

if not login_success:
    print("Login failed, trying to register...")
    register()
retry(booking, 7, "to book")
retry(check_bookings, 7, "to check your bookings")

