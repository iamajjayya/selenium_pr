

from selenium import webdriver
from  selenium.webdriver.common.by import By
import time

'''
text ->  returns only the inner text of the element 
get_attribute -> returns values of any attribute of web element 


'''

driver  =  webdriver.Chrome()
driver.get('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')

email_box  =  driver.find_element(By.XPATH,"//input[@id = 'Email']")
email_box.clear()
email_box.send_keys('admin@yourstore.com')

print("Result of text",email_box.text)
print('Result of get attribute', email_box.get_attribute('value'))
time.sleep(5)
print("Data val required",  email_box.get_attribute('data-val-required'))


button_ele =  driver.find_element(By.XPATH,"//button[text()='Log in']")

print("Text of button", button_ele.text)
print("Class attribute",  button_ele.get_attribute('class'))

driver.quit()