# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome()

# driver.get('https://testautomationpractice.blogspot.com/')

# time.sleep(4)
# # Locate the table
# table = driver.find_element(By.TAG_NAME, "table")

# # Fetch all rows from the table
# rows = table.find_elements(By.TAG_NAME, "tr")

# # Iterate through each row and print the columns
# for row in rows:
#     columns = row.find_elements(By.TAG_NAME, "td")  # Fetch all columns in the row
#     row_data = [col.text for col in columns]  # Extract text from each column
#     print(" | ".join(row_data))  # Print row as a formatted string

# time.sleep(4)
# # Close the browser
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Initialize WebDriver
# driver = webdriver.Chrome()

# # Open the webpage (Replace with the actual URL containing the table)
# driver.get('https://testautomationpractice.blogspot.com/')

# # Locate the table
# table = driver.find_element(By.TAG_NAME, "table")

# # Fetch the headers (th elements)
# headers = table.find_elements(By.TAG_NAME, "th")
# header_names = [header.text for header in headers]  # Extract text from headers

# # Print the headers
# print(" | ".join(header_names))
# print("-" * 50)  # Just a separator for better readability

# # Fetch all rows from the table (excluding headers)
# rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # Skip the first row (header row)

# # Iterate through each row and print the columns
# for row in rows:
#     columns = row.find_elements(By.TAG_NAME, "td")  # Fetch all columns in the row
#     row_data = [col.text for col in columns]  # Extract text from each column
#     print(" | ".join(row_data))  # Print row as a formatted string

# # Close the browser
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the webpage (Replace with the actual URL containing the table)
driver.get('https://testautomationpractice.blogspot.com/')

# Locate the table
table = driver.find_element(By.TAG_NAME, "table")

# Fetch the headers (th elements)
headers = table.find_elements(By.TAG_NAME, "th")
header_names = [header.text for header in headers]  # Extract text from headers

# Choose the column index (e.g., Price column → index 3)
column_name = "Price"  # Change this to the column you want to extract
column_index = header_names.index(column_name)  # Find the index of the chosen column

# Print the column name
print(f"{column_name} Column:")
print("-" * 20)

# Fetch all rows from the table (excluding headers)
rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # Skip the header row

# Iterate through each row and print only the selected column
for row in rows:
    columns = row.find_elements(By.TAG_NAME, "td")  # Fetch all columns in the row
    print(columns[column_index].text)  # Print the specific column

# Close the browser
driver.quit()
