import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("https://pranjalmaurya.vercel.app/")
print(driver.title)

name_field = driver.find_element(By.NAME, "name")
email_field = driver.find_element(By.NAME, "email")
desc_field = driver.find_element(By.NAME, "desc")


name_field.send_keys("John Doe")
email_field.send_keys("john.doe@example.com")
desc_field.send_keys("This is a test message.")

submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
submit_button.click()

time.sleep(15)

driver.quit()
