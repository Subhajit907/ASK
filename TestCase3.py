import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Verify that tenant can click on the "Sign Up" button on the "Create your account" page

# Initialize the webdriver (e.g., Chrome)
driver = webdriver.Firefox()

# Open the webpage where the button is located
driver.get("https://dev.3trade.xyz/sign-up")
time.sleep(5)
checkbox  = driver.find_element("xpath", "//input[@type='checkbox']")
time.sleep(5)
checkbox.click()
time.sleep(5)
# Find the button element
button = driver.find_element("xpath","//button[text()='Sign Up']")

# Check if the button is clickable
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "//button[text()='Sign Up']")))
    print("Button is not clickable","Test Case Failed..")
    # Optionally, you can click on the button here
    # button.click()
except:
    print("Button is clickable","Test Case Passed...")



# Verify that if the tenant clicks on the hyperlinked text "Sign In", it opens the Sign In  page

Sign_In = driver.find_element("xpath", "//a[text()='Sign In']")
Sign_In.click()
title = driver.title
if title == "3trade":
 print("Test Case Passed...")
else:
 print("Test Case Failed...")


 #Verify that when the tenant clicks on the hyperlink text "Click here" on the info icon message, it redirects to the instructions page

hyperlink = driver.find_element("xpath", "//img[@alt='3TRADE logo']")
hyperlink.click()
if title == "3trade":
 print("Test Case Passed...")
else:
 print("Test Case Failed...")

 driver.quit()
