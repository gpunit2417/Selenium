# print the entire table without headers

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com")

# table = driver.find_element(By.ID, 'taskTable')

# rows = table.find_elements(By.TAG_NAME, 'tr')

# for row in rows:
#     columns = row.find_elements(By.TAG_NAME, 'td')
#     row_data = [col.text for col in columns]
#     print(" | ".join(row_data))

# driver.quit()


# print the entire table with headers as well

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# drive = webdriver.Chrome()
# drive.get("https://testautomationpractice.blogspot.com")

# table = drive.find_element(By.ID, 'taskTable')

# header = table.find_elements(By.TAG_NAME, 'th')
# header_name = [head.text for head in header]
# print(" | ".join(header_name))
# print('-' * 30)

# rows = table.find_elements(By.TAG_NAME, 'tr')[1:]

# for row in rows:
#     columns = row.find_elements(By.TAG_NAME, 'td')
#     row_data = [col.text for col in columns]
#     print(" | ".join(row_data))

# drive.quit()


#  print the specific row of the table

# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com")

# table = driver.find_element(By.ID, 'taskTable')

# rows = table.find_elements(By.TAG_NAME, 'tr')[1:]
# row_index = 2

# selected_row = rows[row_index]

# columns = selected_row.find_elements(By.TAG_NAME, 'td')
# row_data = [col.text for col in columns]

# print(f"The data in row index {row_index} is: {row_data}" )


#  print the specific column of the table

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")

table = driver.find_element(By.ID, 'taskTable')

headers = table.find_elements(By.TAG_NAME, 'th')
header_names = [header.text for header in headers]
column_name = "Name"
column_index = header_names.index(column_name)

print(f"{column_name}:")
print('*' * 20)

rows = table.find_elements(By.TAG_NAME, 'tr')[1:]

for row in rows:
    columns = row.find_elements(By.TAG_NAME, 'td')
    print(columns[column_index].text)
