'''

webtable

static webtable
dynamic webtable

'''

from selenium import  webdriver
from selenium.webdriver.common.by import By

'''
1, Count number of rows and columns
2, Read specific row and column data
3, read all the rows and columns data
4, read the data based on condition
'''

driver   = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
Number_of_rows= len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr'))
print("Length of number of rows", Number_of_rows)
number_of_columns = len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//th'))
print("Length of Number of Columns", number_of_columns)

#Read specific row and column data
data  =  driver.find_element(By.XPATH,'//table[@name="BookTable"]//tr[5]/td[3]').text
print("Data", data)
assert data == "Selenium" , " invalid text"

# Tabledata  =  driver.find_element(By.XPATH,'//table[@name="BookTable"]').text
# print(Tabledata)

# 3, read all the rows and columns data

print("Printing all rows and cols data")

for r in range(2, Number_of_rows+1):
    for c in range(1,number_of_columns+1):
        data  =  driver.find_element(By.XPATH,f"//table[@name='BookTable']//tr[{r}]/td[{c}]").text
        print(data, end="   ")
    print()

# 4, read the data based on condition

for r in range(2,Number_of_rows+1):
    author= driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[{r}]/td[2]").text
    if author == "Mukesh":
         book = driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[{r}]/td[1]").text
         prices = driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[{r}]/td[4]").text
         print(book," ", author," ", prices)





driver.quit()
