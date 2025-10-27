from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

ch_op = Options()
# ch_op.add_argument("--disable-notifications")
ch_se =  Service()

driver =  webdriver.Chrome(service=ch_se,options=ch_op)
driver.get("https://whatmylocation.com")


driver.quit()