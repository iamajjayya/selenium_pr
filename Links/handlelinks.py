from selenium import  webdriver
from selenium.webdriver.common.by import By
import time


driver  = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# time.sleep(5)
# #click on link
# driver.find_element(By.LINK_TEXT,'Digital downloads').click()
# time.sleep(5)

links = driver.find_elements(By.XPATH,'//a')
# print(len(links))
#
# for link in links:
#     print(link.text)









#close the session
driver.quit()