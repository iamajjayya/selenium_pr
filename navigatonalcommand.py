'''
Navgational Commnads

back()
forward()
refresh()

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get('https://www.snapdeal.com/')
time.sleep(2)
driver.get('https://www.amazon.in/ref=nav_logo')
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.back()
time.sleep(2)
driver.quit()

