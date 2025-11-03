import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
country_list  =  driver.find_elements(By.XPATH,"//li[@class ='select2-results__option']")
print(len(country_list))

for country in country_list:
    if country.text == "India":
        country.click()
        break



time.sleep(5)


