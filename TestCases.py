from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://dev.3trade.xyz/sign-in?redirectUrl=/")

# Navigate to the login page
driver.get("https://dev.3trade.xyz/sign-in?redirectUrl=/")
time.sleep(5)
driver.maximize_window()

#Verify that when the tenant clicks on the hyperlink text "Sign up" on the Sign In page, it opens the "Technical Prerequisites for 3TRADE Registration" page

driver.find_element("xpath","//a[@class='text-indigo-600 hover:underline !text-[#2970FF]']").click()
time.sleep(5)
Title = driver.find_element("xpath","//div[@class='flex items-center text-[#121926] dark:text-[#FCFCFD] text-[18px] font-[600] leading-[27px]']")
Actual_Text = Title.text
Expacted_Title = "Technical Prerequisites for 3TRADE Registration"
if Actual_Text == Expacted_Title:
 print("Test Case Passed...")
else:
 print("Test Case Failed")


#Verify that when the tenant click on the "Continue to Sign-up" button, it opens the "Create your account" page.

driver.find_element("xpath","//button[text() = 'Continue to Sign-up']").click()
time.sleep(5)
Title = driver.find_element("xpath","//h3[text() = 'Create your account']")
Actual_Text = Title.text
Expacted_Title = "Create your account"
if Actual_Text == Expacted_Title:
 print("Test Case Passed...")
else:
 print("Test Case Failed")


#Verify that the tenant can click on the check box on the Create your account page

checkbox  = driver.find_element("xpath", "//input[@type='checkbox']")
checkbox.click()
# Verify if the checkbox is selected
if checkbox.is_selected():
 print("Test Case Passed...")
else:
 print("Test Case Failed...")


#Verify that when the tenant clicks on the hyperlinked text "User Agreement", it redirects the tenant to the "User Agreement" page

user_agreement_link = driver.find_element("xpath", "//a[text() = 'User Agreement']")
user_agreement_link.click()
current_window_handle = driver.current_window_handle
window_handles = driver.window_handles
# Switch focus to the newly opened tab
for handle in window_handles:

    if handle != current_window_handle:
        driver.switch_to.window(handle)
        break

# Verify if the URL has changed to the "User Agreement" page

if "user_agreement_page" in driver.current_url:
  print("Redirection successful. User Agreement page opened.")
else:
  print("Redirection failed. User Agreement page not opened.")


driver.quit()



