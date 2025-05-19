from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Config Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
service = Service('./chromedriver.exe')  # the location of Chromedriver.exe
driver = webdriver.Chrome(service=service, options=chrome_options)



# Acessar o site
driver.get("https://wwww.facebook.com")
time.sleep(2)  # Wait for the page to load

# Fill in the login form
f_name = driver.find_element(By.ID, "email")
f_name.send_keys("name@gmail.com")
pwl = driver.find_element(By.ID, "pass")
pwl.send_keys("password")
time.sleep(2)  

button = driver.find_element(By.NAME, "login")
button.click()  # Click the login button
time.sleep(100)  # Wait for the page to load

# Close the browser
driver.quit()
