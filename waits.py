'''

waits

types of waits

time.sleep() -> performance of the script is very poor
             ->  if the element is not available within the time mentioned, still there is a chance of getting exception

1, implicit wait
   advantage
    ->  single statement

    dis -advantage ->
                 ->  if the element is not available within the time mentioned, still there is a chance of getting exception

2, explict wait
   -> Waits for a specific condition for a specific element.
  -> explict wait works in condition
'''
import time
from selenium import  webdriver
from selenium.webdriver.common.by import By



driver  = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get('https://www.google.com/')
driver.maximize_window()
searchBox =  driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")

searchBox.send_keys('selenium')
searchBox.submit()
# time.sleep(10)
driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()



driver.quit()





