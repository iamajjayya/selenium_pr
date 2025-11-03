import os
from selenium import  webdriver
from selenium.webdriver.common.by import By
location = os.getcwd()
driver  =  webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

screnshot_path  =  os.path.join(location,"fullpage.png")

# driver.save_screenshot(screnshot_path)
# driver.get_screenshot_as_file("v2.png")

# element = driver.find_element(By.XPATH,"//img[@alt ='Picture of Build your own computer']")
# element.screenshot(screnshot_path)

totol_width  =  driver.execute_script("return document.body.scrollWidth")
total_height =  driver.execute_script("return document.body.scrollHeight")

driver.set_window_size(totol_width,total_height)
driver.save_screenshot(screnshot_path)
