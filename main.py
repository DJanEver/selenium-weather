from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "E:/users/hakee/programmingstuff/chromedriver.exe"
DRIVER = webdriver.Chrome(CHROME_DRIVER_PATH)

def loadWeather(siteUrl):
    DRIVER.get(siteUrl)
    element = DRIVER.find_element(By.NAME, 'q')
    element.send_keys("weather forecast kingston" + Keys.RETURN)


if __name__ == '__main__':
    loadWeather("http://www.google.com")


