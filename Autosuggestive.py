import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver


obj= Service("C:/Users/Emilmariya/Documents/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=obj)
#driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)
#driver.find_element(By.LINK_TEXT,"India").click()
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    country.click()
    break
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"