from Driver import WebDriver
from selenium.webdriver.common.by import By
from BRDData import BRDDriver

driver = WebDriver()
def getFinancialData():
  brdDriver = BRDDriver(driver)

  # table = driver.searchElement(By.ID, 'tabAccountExchangeRates')
  # if not table:
  #   return 
  # childTables = driver.children(table)
  # if not len(childTables):
  #   return
  
  # financialDivs = driver.children(childTables[0])
  # for a in financialDivs:
  #   print(a.tag_name)

getFinancialData()


