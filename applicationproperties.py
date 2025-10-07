from selenium import  webdriver

driver  = webdriver.Chrome()

driver.get('https://www.google.com')

print("Page Title",  driver.title)
print("Page URL", driver.current_url)
print("Page source", driver.page_source)

driver.quit()