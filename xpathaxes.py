from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver =  webdriver.Chrome()
driver.get("https://www.moneycontrol.com/stocksmarketsindia/")
driver.maximize_window()

#self
# textmsg  =  driver.find_element(By.XPATH,"//a[text() ='NIFTY BANK']//self::a").text
# print(textmsg)

# get_title =  driver.title
# print(get_title)
# #parent
# text_msg =  driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/parent::td").text
# print(text_msg)

# #child
# text_msg = driver.find_elements(By.XPATH,"//a[text() ='NIFTY BANK']//ancestor::tr//child::td")
# print(len(text_msg))


# text_msg = driver.find_element(By.XPATH,"//a[text() ='NIFTY BANK']//ancestor::tr//child::td[2]").text
# print(text_msg)

# #ancestor
# text_msg  = driver.find_element(By.XPATH,"//a[text() ='NIFTY BANK']//ancestor::tr").text
# print(text_msg)

#desendent
# text_msg  = driver.find_element(By.XPATH,"//a[text() ='NIFTY BANK']//ancestor::tr//descendant::td[4]").text
# print(text_msg)

#following
# text =  driver.find_elements(By.XPATH,"//a[contains(text(),'NIFTY IT')]//ancestor::tr//following::*")
# print(len(text))

#following-sibiling
# text = driver.find_elements(By.XPATH,"//a[contains(text(),'NIFTY IT')]//ancestor::tr//following-sibling::*")
# print(len(text))

#preceding
# text = driver.find_elements(By.XPATH,"//a[contains(text(),'NIFTY IT')]//ancestor::tr//preceding::*")
# print(len(text))

#preceding-sibling
text  = driver.find_elements(By.XPATH,"//a[contains(text(),'NIFTY IT')]//ancestor::tr//preceding-sibling::*")
print(len(text))

driver.quit()