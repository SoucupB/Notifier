from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WebDriver():
  def __init__(self, maxWaitPerElement = 10):
    options = Options()
    options.add_argument("--headless=new")
    self.service = Service('Engine/chromedriver.exe')
    self.driver = webdriver.Chrome(service=self.service, options=options)
    self._isOpened = False
    self.maxWaitPerElement = maxWaitPerElement * 1000

  def open(self, url):
    self.driver.get(url)
    WebDriverWait(self.driver, self.maxWaitPerElement).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    print("Page loaded!")
    self._isOpened = True

  def searchElement(self, by, value):
    if not self._isOpened:
      return
    element = None
    currentTime = int(time.time() * 1000)
    while True:
      try:
        element = WebDriverWait(self.driver, self.maxWaitPerElement / 1000).until(
          EC.presence_of_element_located((by, value))
        )
      except:
        pass
      if element:
        break
      if int(time.time() * 1000) - currentTime > self.maxWaitPerElement:
        break
      time.sleep(1)

    return element
  
  def children(self, element):
    response = []
    children = element.find_elements(By.XPATH, './*')
    for child in children:
      response.append(child)

    return response
      