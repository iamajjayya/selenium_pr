'''

is_displayed()
is_enables()
is_selected()



check the status of the element

'''

from selenium import  webdriver
from selenium.webdriver.common.by import  By

driver  = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()


#is_displayed() is_enabled
searbox_element  = driver.find_element(By.XPATH, "//*[@id='small-searchterms']")
print("Element displayed",searbox_element.is_displayed())
print("Element is_enabled", searbox_element.is_enabled())


#is_selected

radio_element =  driver.find_element(By.XPATH,"//*[@id='gender-male']")
print('Element displayed', radio_element.is_displayed())
print('Element is_enabled', radio_element.is_enabled() )

print(radio_element.is_selected())
if radio_element.is_selected():
    print("radio_element Male is selected")
else:
   radio_element.click()


print("Male radio button is selected ? ",  radio_element.is_selected())
driver.execute_script("arguments[0].checked=false", radio_element)
print(radio_element.is_selected())






driver.quit()