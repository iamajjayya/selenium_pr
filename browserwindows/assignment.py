

from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

driver  = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("Selenium")

driver.find_element(By.XPATH,"//input[@type='submit']").click()


time.sleep(3)
links = driver.find_elements(By.CSS_SELECTOR,"#Wikipedia1_wikipedia-search-results a")


for link in links:
        link.click()


        time.sleep(2)

windowid  = driver.window_handles

for winid in windowid:
    driver.switch_to.window(winid)
    if driver.title == "Selenium in biology - Wikipedia" and driver.title == "Selenium - Wikipedia":
        time.sleep(2)
        driver.close()

    print(driver.title)

for winid in windowid:
    driver.switch_to.window(winid)
    print("Second time" ,  driver.title)

time.sleep(5)

driver.quit()