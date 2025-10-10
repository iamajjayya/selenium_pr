from http.client import responses

import requests
from selenium import  webdriver
from selenium.webdriver.common.by import By

driver  = webdriver.Chrome()
driver.get('http://www.deadlinkcity.com/')

links = driver.find_elements(By.TAG_NAME,'a')
count  = 0
for link in links:
    url =  link.get_attribute('href')

    if url is None or url.strip() == '':
        continue

    try:
        responses  = requests.get(url, timeout=5)
        if responses.status_code >=  400:
            print(f"Broken Link {link} and {responses.status_code}")
            count += 1
        else:
            print(f"Working link {link} and {responses.status_code}")

    except Exception as e:
        print(e)

print(count)