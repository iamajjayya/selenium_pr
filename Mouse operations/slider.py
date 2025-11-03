import time

from  selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains

driver  = webdriver.Chrome()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

min_slider = driver.find_element(By.XPATH,"//div[@id='slider-range']//span[1]")
max_slider = driver.find_element(By.XPATH,"//div[@id='slider-range']//span[2]")

print("Location of sliders Before Moving")
print(min_slider.location)
print(max_slider.location)

ac = ActionChains(driver)
ac.drag_and_drop_by_offset(min_slider,60,0).perform()
ac.drag_and_drop_by_offset(max_slider,-39,0).perform()
time.sleep(5)

driver.quit()

