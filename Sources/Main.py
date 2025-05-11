from Driver import WebDriver
from selenium.webdriver.common.by import By
from BRDData import BRDDriver

driver = WebDriver()
def getFinancialData():
  brdDriver = BRDDriver(driver)
  print(brdDriver.data['EUR'])

getFinancialData()


