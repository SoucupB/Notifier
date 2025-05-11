from Driver import WebDriver
from selenium.webdriver.common.by import By
from BRDData import BRDDriver
from Email import EmailDriver
import os
from dotenv import load_dotenv
load_dotenv()
driver = WebDriver()
def getFinancialData():
  brdDriver = BRDDriver(driver)
  response = ""
  for key, value in brdDriver.data.items():
    response += f"<p>Currency: {key}, Selling by: {value['sell_value']}, Buying by: {value['buy_value']}</p>"
  eml = EmailDriver()
  eml.basicSend(os.getenv("EMAIL_SEND_TO"), "Currency data", response)

getFinancialData()
print("DONE!")


