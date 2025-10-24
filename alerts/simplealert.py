import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver =  webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()

alert = driver.switch_to.alert

time.sleep(5)

print(alert.text)
alert.send_keys("Hello Ajay")
alert.dismiss()

time.sleep(5)

# result =  driver.find_element(By.XPATH,"//p[text()='You successfully clicked an alert']").text

# assert result == 'You successfully clicked an alert', 'Result failed'

# time.sleep(5)