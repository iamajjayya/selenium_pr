from selenium import  webdriver
from selenium.webdriver.common.by import By


driver  = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')


# print(len(cookies))
# print(cookies,  end="")
# for c in cookies:
#     print(c.get('name'), c.get("value"))
#
#
#Add new cookie to the browser
driver.add_cookie({
    "name" : "Mycookies",
    "value":"1234567"
})
cookies = driver.get_cookies()
print(len(cookies))

driver.delete_cookie('Mycookies')
print(len(cookies))
cookies = driver.get_cookies()
print(len(cookies))
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))








driver.quit()

