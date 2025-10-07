'''

find_element

* A single webElement the first matching element it finds
* If Multiple elements match, only the first one is returned


find_elements

* A list of webElements
* if multiple elements match, all are returned in a list
* if no element found, return an empty list

'''

from selenium import webdriver
from selenium.webdriver.common.by import By


driver  =  webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')

# #1) Locator matching single element
# element = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Phones")
# driver.find_element(By.XPATH, "//button[text() =  'Search']").click()

#2) Locator matching with multiple  elements
# element = driver.find_element(By.XPATH,"//*[@class='footer']//a")
# print(element.text)


# elements = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))

# element = driver.find_elements(By.XPATH,"//*[@class='footer']//a")
# print(len(element))
#
# element = driver.find_element(By.XPATH,"//*[@class='oter']//a")
# print(element.text)




element = driver.find_elements(By.XPATH,"//*[@class='footer']//a")
print(len(element))
print(element[0].text)

for el in element:
    print(el.text)





driver.quit()



