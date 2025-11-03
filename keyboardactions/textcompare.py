import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains
from selenium.webdriver.common.keys import Keys
driver  =  webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.implicitly_wait(5)
driver.maximize_window()
input1 = driver.find_element(By.ID,"inputText1")
input2 = driver.find_element(By.ID,"inputText2")
input1.send_keys("Welcome to selenium ")

ac = ActionChains(driver)

#Ctrl+A
ac.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#CTRL C
ac.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#PRESS TAB
ac.key_down(Keys.TAB).key_up(Keys.TAB).perform()

#CTRL V
ac.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

time.sleep(5)


