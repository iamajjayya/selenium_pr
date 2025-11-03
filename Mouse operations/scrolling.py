import time
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver =  webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.worldometers.info/geography/alphabetical-list-of-countries/")

# #1. scroll down page by pixel
#
# driver.execute_script("window.scrollBy(0,6000)")
# value = driver.execute_script("return window.pageYOffset;")

# #2 scroll down page till the element is visible
# flag = driver.find_element(By.XPATH,"//td[normalize-space() ='India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag),

#scroll down the page till end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(4)



driver.quit()