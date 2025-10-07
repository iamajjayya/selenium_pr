from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
#tagname#valueofid

# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")

# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")

#attribute
#tagname[attribute=value]
# driver.find_element(By.CSS_SELECTOR,"input[placeholder=Email]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Email or phone number"]').send_keys("abc@gmail.com")

driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-email]").send_keys("abc@gmail.com")


time.sleep(3)




