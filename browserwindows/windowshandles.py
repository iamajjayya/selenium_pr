'''

-> Selenium creates one browser window or tab this is your main window or parent window
but sometimes when u click  alinks or button a new window or tab opens - thats a child window

commands

driver.current_window_handle  =  return the handle (unique ID ) of the current window
driver.window_handles  = returns a list o all open window handles
driver.switch_to.window(handle) => switches control to a specific window
driver.close() => close the current window
driver.quit()  = closes all browser windows opened by selenium

'''


from selenium import  webdriver
from selenium.webdriver.common.by import By
import time


driver  = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(5)
driver.implicitly_wait(10)
driver.maximize_window()
windlowhandler =  driver.current_window_handle

print(windlowhandler)

driver.find_element(By.XPATH,'//a[normalize-space() ="OrangeHRM, Inc"]').click()
time.sleep(5)
windowsId =  driver.window_handles


#approaches 1
# parentwindowid  = windowsId[0]
# childwindowid = windowsId[1]
#
# # print(parentwindowid, childwindowid)

#Appproches 2

# for  winid in windowsId:
#     driver.switch_to.window(winid)
#     print(driver.title)



#
# driver.switch_to.window(childwindowid)
# print("Title of the Child window",driver.title)
#
# driver.switch_to.window(parentwindowid)
# print("Driver of parent window",driver.title)

for  winid in windowsId:
    driver.switch_to.window(winid)
    print(driver.title)
    if driver.title == "Human Resources Management Software | HRMS | OrangeHRM" and driver.title == "OrangeHRM":
        driver.close()
