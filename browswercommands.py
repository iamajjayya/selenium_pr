'''

close () ->  close single browser window(where driver focused)
quit () -> close all the browser windows

'''


from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver  = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element(By.LINK_TEXT,'Click Here').click()
time.sleep(5)

driver.close()

time.sleep(5)
driver.quit()

