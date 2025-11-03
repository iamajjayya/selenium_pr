from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

ch_op = Options()
ch_op.add_argument("--headless")
ch_se = Service()

driver  = webdriver.Chrome(service= ch_se,  options=ch_op)
driver.get('https://www.dummyticket.com/dummy-ticket-for-visa-application/')
driver.implicitly_wait(5)
print(driver.title, driver.current_url)
driver.quit()