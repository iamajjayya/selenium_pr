import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)


driver.find_element(By.XPATH,'//input[@id ="datepicker"]').click()

year  =  "2021"
month  = "April"
date  =  "22"

Months  = {
    "January" : 1,
    "February": 2,
    "March" : 3,
    "April" :  4,
    "May" : 5,
    "June" :6,
    "July" : 7,
    "August" : 8,
    "September": 9,
    "October":10,
    "November" : 11,
    "December" : 12
}

while True:
    mo = driver.find_element(By.XPATH,'//span[@class = "ui-datepicker-month"]').text
    ye = driver.find_element(By.XPATH,'//span[@class = "ui-datepicker-year"]').text

    if mo == month and ye == year:
        break

    elif (ye < year)  or (ye == year and Months[mo] < Months[month]):
        driver.find_element(By.XPATH, '//span[@class = "ui-icon ui-icon-circle-triangle-e"]').click()
    else:
        driver.find_element(By.XPATH,'//span[@class ="ui-icon ui-icon-circle-triangle-w"]').click()






#select date
dates =  driver.find_elements(By.XPATH,'//table[@class ="ui-datepicker-calendar"]//tbody//tr//td/a')

for ele in dates:
    if ele.text == date:
        ele.click()

time.sleep(5)


