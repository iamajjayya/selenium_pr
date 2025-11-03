import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver  = webdriver.Chrome()
driver.get('https://seleniumbase.io/w3schools/double_click')
driver.maximize_window()
driver.switch_to.frame(0)
doubleclick =  driver.find_element(By.XPATH,'//p[@ondblclick="myFunction()"]')

ac  = ActionChains(driver)
ac.double_click(doubleclick).perform()


time.sleep(5)
driver.quit()


