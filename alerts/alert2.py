import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver =  webdriver.Chrome()

driver.get("https://webmail.rediffmailpro.com/action/login/classociates.in")

driver.maximize_window()
time.sleep(5)
driver.get("https://webmail.rediffmailpro.com/action/login/classociates.in")
driver.find_element(By.XPATH,"//input[@type='image']").click()
alert =  driver.switch_to.alert
print(alert.text)
time.sleep(5)
alert.accept()

driver.quit()