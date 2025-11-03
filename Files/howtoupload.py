import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver  =  webdriver.Chrome()
driver.get('https://www.file.io/')
driver.maximize_window()

upload_input = driver.find_element(By.ID,'select-files-input')
upload_input.send_keys(r"C:/Users/ajjay/Downloads/sample-1.pdf")
time.sleep(5)
driver.quit()
