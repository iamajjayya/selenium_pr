import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import  expected_conditions as ec

driver  = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
Number_of_rows = len(driver.find_elements(By.XPATH,"//table[@id='taskTable']//tr"))
print(Number_of_rows)

Number_of_coloums  = len(driver.find_elements(By.XPATH,"//table[@id='taskTable']//th"))
print(Number_of_coloums)

for r in range(1, Number_of_rows):
    name =  driver.find_element(By.XPATH,f"//table[@id='taskTable']//tr[{r}]/td").text
    if name == "Chrome":
        memory_data  =  driver.find_element(By.XPATH,f"//table[@id='taskTable']//tr/td[{r}]").text
        print(memory_data)


driver.quit()
