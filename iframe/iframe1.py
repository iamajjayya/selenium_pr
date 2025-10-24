'''

Frame and Iframe

Frame -> A frame is an HTML document embedded inside another HTML document.

How to handle Frames in selenium
-> driver.switch_to.frame()

we can switch to frame by 3 ways
1, By Index
2, By name or Id
3, By web element

Switching back to the main Page
switch to parent Frame
driver.switch_to.parent_frame()

switch to default content
driver.switch_to.default_content()


'''

from selenium import  webdriver
from selenium.webdriver.common.by import  By


driver  = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/nested_frames")
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-middle")
framename  = driver.find_element(By.XPATH,"//body").text
print(framename)
driver.switch_to.parent_frame()
driver.switch_to.frame("frame-left")
left = driver.find_element(By.XPATH,'//body').text
driver.switch_to.parent_frame()
print(left)
driver.switch_to.frame("frame-right")
right =  driver.find_element(By.XPATH,"//body").text
print(right)
driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
bottom = driver.find_element(By.XPATH,"//body").text
print(bottom)

driver.quit()















