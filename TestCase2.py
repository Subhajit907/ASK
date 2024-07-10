from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Verify that the tenant can add a valid business email and valid organization name in the field boxes of the Create your account page

try:
    driver = webdriver.Firefox()

    driver.get("https://dev.3trade.xyz/sign-up")

    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("xpath", "//input[@class='input input-md h-11 input-invalid']")
)
    )

    checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    checkbox.click()

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    verification = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(("xpath", "//input[@class='input input-md h-11 input-invalid']")
)
    )

    actual_text = verification.text
    expected_text = "Please enter your organization name"

    if actual_text == expected_text:
        print("TestCase Passed...")
    else:
        print("TestCase Failed...")

except NoSuchElementException as e:
    print("Element not found: ", e)
except TimeoutException as e:
    print("Timeout waiting for element: ", e)
finally:

    driver.quit()