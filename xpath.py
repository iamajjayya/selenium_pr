from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver =  webdriver.Chrome()
driver.get("https://www.automationexercise.com/products")
driver.maximize_window()
# driver.find_element(By.XPATH,"/html/body/section/div/input").clear()
# driver.find_element(By.XPATH,"/html/body/section/div/input").send_keys("shirts")
# driver.find_element(By.XPATH,"/html/body/section/div/button").click()

driver.find_element(By.XPATH, "//*[@name='search']").clear()
driver.find_element(By.XPATH, "//*[contains(@id, 'product')]").send_keys("shirts")
driver.find_element(By.XPATH,"//*[starts-with(@id, 'submit_search')]").click()


time.sleep(5)
driver.execute_script("window.scrollBy(0,500)")
time.sleep(5)
driver.quit()