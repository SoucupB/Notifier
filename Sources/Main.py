from Driver import WebDriver
from selenium.webdriver.common.by import By
from BRDData import BRDDriver
from Email import EmailDriver

# driver = WebDriver()
def getFinancialData():
  # brdDriver = BRDDriver(driver)
  # print(brdDriver.data['EUR'])
  eml = EmailDriver()
  eml.basicSend("soucup.bogdan@gmail.com", "Test subject", "Yolo data")

getFinancialData()


