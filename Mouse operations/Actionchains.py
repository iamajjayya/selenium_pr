'''
Mouse Operations

ActionsChains

1, Mouse over ->  move_to_element(element)
2, Right click ->  context_click(element)
3, Double click -> double_click(doubleclick)
5, Drag and Drop -> drag_and_drop(sourece,destination)
6, slider -> drag_and_drop_by_offset(max_slider,x,y)

scrolling page 

'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import  ActionChains

driver  = webdriver.Chrome()
driver.get("https://practice.expandtesting.com/hovers")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//input[@name = 'username']").send_keys("admin")
# driver.find_element(By.XPATH,"//input[@name = 'password']").send_keys("admin123")
# driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
driver.maximize_window()

view_profile = driver.find_element(By.XPATH,"//main[@class='flex-shrink-0 py-3']//div[@class='container']//div[1]//div[1]//a[1]")
profile  =  driver.find_element(By.XPATH,"//img[@data-testid='img-user-1']")
profile2 =  driver.find_element(By.XPATH, "//img[@data-testid='img-user-2']")
time.sleep(5)
print(driver.title)
act = ActionChains(driver)
act.move_to_element(profile).perform()
act.move_to_element(profile2).perform()
print(driver.title)

time.sleep(5)

driver.quit()






