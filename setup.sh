@echo off
echo Installing Python...
choco install python --confirm
echo Installing WebDriver Manager...
pip install webdriver-manager
echo Installing Python dependencies...
pip install -r requirements.txt
echo Installing ChromeDriver...
pip install chromedriver-autoinstaller
echo Installing Google Chrome...
choco install googlechrome --confirm

echo Setup Complete!
