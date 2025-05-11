from Driver import WebDriver
from selenium.webdriver.common.by import By
from BRDData import BRDDriver
from Email import EmailDriver
import os
from dotenv import load_dotenv
load_dotenv()
# driver = WebDriver()
def getFinancialData():
  print(os.getenv('SECRET_KEY'))
  # brdDriver = BRDDriver(driver)
  # print(brdDriver.data['EUR'])
  # eml = EmailDriver()
  # eml.basicSend(os.getenv("EMAIL_SEND_TO"), "Test subject", "Yolo data")

getFinancialData()

print("DONE!")


