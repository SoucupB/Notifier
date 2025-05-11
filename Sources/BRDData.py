from Driver import WebDriver
from selenium.webdriver.common.by import By

class BRDDriver():
  def __init__(self, driver):
    self.driver = driver
    self.driver.open("https://www.brd.ro/curs-valutar-si-dobanzi-de-referinta")
    self.data = {}
    self._loadData()

  def _loadCurrencies(self, parent):
    self.currencyValues = []
    index = 0
    for curr in parent:
      if not index:
        index += 1
        continue
      val = curr.get_attribute('innerText')
      self.data[val] = {}
      self.currencyValues.append(val)
      index += 1

  def _loadValues(self, parent, key):
    index = 0
    for curr in parent:
      if not index:
        index += 1
        continue
      val = curr.get_attribute('innerText')
      self.data[self.currencyValues[index - 1]][key] = val
      index += 1
  def _loadBuyingValue(self, parent):
    self._loadValues(parent, 'buy_value')

  def _loadSellingValue(self, parent):
    self._loadValues(parent, 'sell_value')
  
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
    currenciesElements = self.driver.children(financialDivs[1])
    self._loadCurrencies(currenciesElements)
    buyingValue = self.driver.children(financialDivs[3])
    self._loadBuyingValue(buyingValue)
    sellingValue = self.driver.children(financialDivs[4])
    self._loadSellingValue(sellingValue)