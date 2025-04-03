# print the entire table without headers

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")

table = driver.find_element(By.ID, 'taskTable')

rows = table.find_elements(By.TAG_NAME, 'tr')

for row in rows:
    columns = row.find_elements(By.TAG_NAME, 'td')
    row_data = [col.text for col in columns]
    print(" | ".join(row_data))

driver.quit()
