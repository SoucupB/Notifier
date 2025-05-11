from Driver import WebDriver
from selenium.webdriver.common.by import By

driver = WebDriver()
driver.open("https://www.brd.ro/curs-valutar-si-dobanzi-de-referinta")

crt = driver.searchElement(By.ID, 'tabAccountExchangeRates')

if crt:
  print(f"Found! {crt}")

