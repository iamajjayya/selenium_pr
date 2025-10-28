'''

Date Picker

1, Standard
2, Non - Standard (Customized)



'''
import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@class="demo-frame"]'))
# driver.find_element(By.XPATH,'//input[@id = "datepicker"]').send_keys("12/1/2002")

year = "2022"
month  = "April"
date = "2"

driver.find_element(By.XPATH, '//input[@id = "datepicker"]').click()


months = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12
}

while True:
    mo = driver.find_element(By.XPATH,'//span[@class ="ui-datepicker-month"]').text
    ye =  driver.find_element(By.XPATH, '//span[@class ="ui-datepicker-year"]').text

    if mo == month and ye == year:
        break;

    elif (ye < year) or (ye == year and months[mo] < months[month]):
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

    else:

        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()



#select date

dates  = driver.find_elements(By.XPATH,'//table[@class = "ui-datepicker-calendar"]/tbody//tr//td//a')
for ele in dates:
    if ele.text == date:
        ele.click()
        break


time.sleep(3)







time.sleep(5)

driver.quit()
