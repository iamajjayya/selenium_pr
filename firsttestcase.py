import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")


driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.XPATH,"//button[@type='submit']").click()




# driver.find_element(By.LINK_TEXT,"Logout").click
# driver.find_element(By.PARTIAL_LINK_TEXT,"gout").click()

navbar_names  =  driver.find_elements(By.CLASS_NAME,"has-treeview")
print(len(navbar_names))

a_tags =  driver.find_elements(By.TAG_NAME,"div")
print(len(a_tags))


driver.close()

