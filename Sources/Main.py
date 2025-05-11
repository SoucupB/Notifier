from Driver import WebDriver
from selenium.webdriver.common.by import By

driver = WebDriver()
driver.open("https://www.brd.ro/curs-valutar-si-dobanzi-de-referinta")

def getFinancialData():
  table = driver.searchElement(By.ID, 'tabAccountExchangeRates')
  if not table:
    return 
  childTables = driver.children(table)
  if not len(childTables):
    return
  
  financialDivs = driver.children(childTables[0])
  for a in financialDivs:
    print(a.tag_name)

getFinancialData()


