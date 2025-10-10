from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import time

driver  = webdriver.Chrome()
driver.get('https://practice.expandtesting.com/dropdown')
driver.maximize_window()

dropdown  =  Select(driver.find_element(By.XPATH,"//select[@id='dropdown']"))
dropdown.select_by_index(2)

time.sleep(3)


dropdown.select_by_value('1')

total_np = dropdown.options
print("Total options", len(total_np))


time.sleep(3)

dropdown.select_by_visible_text('Option 1')
selected =  dropdown.first_selected_option
print(selected.text)

for option in dropdown.options:
    print(option.text)

time.sleep(3)


time.sleep(5)

# select option from dropdown without using built in methods

for option in dropdown.options:
    if option.text == 'Option 2':
        option.click()
selec =  dropdown.first_selected_option
print(selec.text)


#close the session
driver.quit()
