from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')

time.sleep(2)

Name = driver.find_element(By.XPATH, "//*[@id='name']")
Name.send_keys("Punit goyal")

time.sleep(2)

Email = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/input[2]").send_keys("punitgoyal106@gmail.com")

time.sleep(2)

Phone = driver.find_element(By.ID, "phone")
Phone.send_keys("9896414101")

time.sleep(2)

address = driver.find_element(By.ID, "textarea")
address.send_keys("Vpo Barwala, near grain market")

time.sleep(2)
gender = driver.find_element(By.XPATH, "//*[@id='post-body-1307673142697428135']/div[3]/div[1]")
gender.click()

time.sleep(12)