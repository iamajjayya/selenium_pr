import time

from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import os
locaation  = os.getcwd()
chrome_option  = Options()
prefreences = {
    "download.default_directory":locaation,
    "download.prompt_for_downloads":False,
    "download.directory_upgrade":True,
    "plugins.always_open_pdf_externally":True
}

chrome_option.add_experimental_option("prefs", prefreences)

chrome_service = Service()


driver = webdriver.Chrome(service=chrome_service,options=chrome_option)
driver.get("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf")

driver.maximize_window()
driver.implicitly_wait(50)
# driver.find_element(By.XPATH,"//a[@href='/samples/documents/word/sample1.doc']").click()
time.sleep(5)
driver.quit()


