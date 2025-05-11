from Driver import WebDriver
from selenium.webdriver.common.by import By

class BRDDriver():
  def __init__(self, driver):
    self.driver = driver
    self.driver.open("https://www.brd.ro/curs-valutar-si-dobanzi-de-referinta")
    self._loadData()
  
  def _loadData(self):
    table = self.driver.searchElement(By.ID, 'tabAccountExchangeRates')
    if not table:
      return 
    childTables = self.driver.children(table)
    if not len(childTables):
      return
    financialDivs = self.driver.children(childTables[0])
    if not len(financialDivs):
      return 
    currencies = self.driver.children(financialDivs[1], 'p')
    for a in currencies:
      print(a.tag_name)