from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://testautomationpractice.blogspot.com/')

time.sleep(4)
# Locate the table
table = driver.find_element(By.TAG_NAME, "table")

# Fetch all rows from the table
rows = table.find_elements(By.TAG_NAME, "tr")

# Iterate through each row and print the columns
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")  # Fetch all columns in the row
    row_data = [col.text for col in columns]  # Extract text from each column
    print(" | ".join(row_data))  # Print row as a formatted string

time.sleep(4)
# Close the browser
driver.quit()
