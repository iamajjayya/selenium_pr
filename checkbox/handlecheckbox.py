from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver =  webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

#1) select specific element
driver.find_elements(By.XPATH,"//input[@class='form-check-input']")

checkboxes = driver.find_elements(By.XPATH,"//input[@class='form-check-input' and  contains(@id,'day')]")

#
# for check in checkboxes:
#     weekname = check.get_attribute('id')
#     if weekname == 'sunday' or weekname == 'tuesday':
#         check.click()
#
#     print(weekname)

# for i in range(len(checkboxes)):
#     checkboxes[i].click()

print(len(checkboxes))

#slect last two checkbox

for i in range(len(checkboxes)-2, len(checkboxes)):
    checkboxes[i].click()

time.sleep(5)

#clearing all the checkbox
for check in checkboxes:
    check.click()
    if check.is_selected():
        check.click()


driver.quit()
