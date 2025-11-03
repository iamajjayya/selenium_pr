import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains


driver  =  webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

right_button = driver.find_element(By.XPATH,"//span[@class ='context-menu-one btn btn-neutral']")

act = ActionChains(driver)
act.context_click(right_button).perform()
time.sleep(5)
driver.quit()