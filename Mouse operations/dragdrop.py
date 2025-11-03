import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver  =  webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.switch_to.frame(0)
sourece  = driver.find_element(By.XPATH,"//img[@alt='The peaks of High Tatras']")
source1 = driver.find_element(By.XPATH,"//*[@alt ='Planning the ascent']")
destination  =  driver.find_element(By.XPATH, "//div[@id ='trash']")

ac  =ActionChains(driver)

ac.drag_and_drop(sourece,destination).perform()
time.sleep(3)
ac.drag_and_drop(source1,destination).perform()

time.sleep(5)

driver.quit()