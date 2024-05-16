import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#obj= Service("C:/Users/Emilmariya/Documents/chromedriver-win64/chromedriver.exe")
#driver = webdriver.Chrome(service=obj)
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

#
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//div/input[@name='name']").send_keys("Emil")
driver.find_element(By.NAME,"email").send_keys("abin@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("1234qwer")
driver.find_element(By.ID,"exampleCheck1").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
Text = driver.find_element(By.CLASS_NAME,"alert-success").text
print(Text)
assert "Success" in Text
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").clear()
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys("Hello")
time.sleep(3)
