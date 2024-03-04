Using python Selenium automation (https://www.saucedemo.com/)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch the browser and open the website
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Display cookies before login
print("Cookies before login:", driver.get_cookies())

# Perform login
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()

# Wait for the dashboard page to load
time.sleep(2)

# Display cookies after login
print("Cookies after login:", driver.get_cookies())

# Navigate to Zen portal dashboard
driver.get("https://www.example.com/zenportal")

# Perform login on Zen portal (assuming similar login process)
# Insert code to perform login on Zen portal here

# Verify cookies after Zen portal login
print("Cookies after Zen portal login:", driver.get_cookies())

# Close the browser
driver.quit()