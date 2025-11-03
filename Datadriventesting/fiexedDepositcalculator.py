import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Datadriventesting import  excelutils
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

ch_option  = Options()
ch_service = Service()
ch_option.add_argument('--disable-notification')


driver  =  webdriver.Chrome(service=ch_service,options=ch_option)
driver.get('https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html')
driver.implicitly_wait(10)
driver.maximize_window()



file  =  r'C:\Users\ajjay\PycharmProjects\Selenium_practice\Datadriventesting\wdata1.xlsx'
# excelutils.getRowCount(file,'Sheet1')
# excelutils.getColumnCount(file,)

row =  excelutils.getRowCount(file,'Sheet1')

for r in range(2,row+1):
    #reading data from excel
    prinicpal = excelutils.readData(file,'Sheet1',r,1)
    RateofIntrest = excelutils.readData(file,'Sheet1',r,2)
    per1 = excelutils.readData(file,'Sheet1',r,3)
    per2 = excelutils.readData(file,'Sheet1',r,4)
    freq = excelutils.readData(file,'Sheet1',r,5)
    maturity = excelutils.readData(file,'Sheet1',r,6)

    #passing data to the application
    driver.find_element(By.ID,'principal').send_keys(prinicpal)
    driver.find_element(By.ID,'interest').send_keys(RateofIntrest)
    driver.find_element(By.ID,'tenure').send_keys(per1)
    per2drp=Select(driver.find_element(By.ID,'tenurePeriod'))
    per2drp.select_by_visible_text(per2)
    freqdrp =  Select(driver.find_element(By.ID,'frequency'))
    freqdrp.select_by_visible_text(freq)
    driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
    act_value = driver.find_element(By.XPATH,"//*[@id = 'resp_matval']//strong").text

    #Validation

    if float(maturity) == float(act_value):
        print("Test Passed")
        excelutils.WriteData(file,'Sheet1',r,8,"Pass")
        excelutils.fillGreenColour(file,'Sheet1',r,8)
    else:
        print("Test Failed")
        excelutils.WriteData(file,'Sheet1',r,8,'Fail')
        excelutils.fillRedColour(file,'Sheet1',r,8)

    driver.find_element(By.XPATH,"//img[@class='PL5']").click()
    time.sleep(3)

driver.close()










