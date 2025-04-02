from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')

time.sleep(2)

Name = driver.find_element(By.XPATH, "//*[@id='name']")
Name.send_keys("Punit goyal")

time.sleep(10)