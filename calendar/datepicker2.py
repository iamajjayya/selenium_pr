import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver  = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.XPATH,'//input[@id = "appoinmentdate"]').click()

# driver.find_element(By.XPATH,'//*[@class= "ui-datepicker-month"]')
datepicker_month  = Select(driver.find_element(By.XPATH,'//*[@class= "ui-datepicker-month"]'))
datepicker_month.select_by_visible_text("Dec")
datepicker_year = Select(driver.find_element(By.XPATH,'//*[@class= "ui-datepicker-year"]'))
datepicker_year.select_by_visible_text("2002")

date = "23"

dates  =  driver.find_elements(By.XPATH,'//*[@class= "ui-datepicker-calendar"]//tbody/tr//a')

for ele in dates:
    if ele.text  == date:
        ele.click()
        break
time.sleep(6)
driver.quit()
