from selenium import  webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec

driver = webdriver.Chrome()


mywait  = WebDriverWait(driver, 10,ignored_exceptions=[Exception], poll_frequency=2) #explicitywait

driver.get('https://www.google.com/')
driver.maximize_window()
searchBox =  driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")

searchBox.send_keys('selenium')
searchBox.submit()
# time.sleep(10)
selenium_page= mywait.until(ec.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))

'''




'''




