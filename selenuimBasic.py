from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')

# time.sleep(2)
# Name = driver.find_element(By.XPATH, "//*[@id='name']")
# Name.send_keys("Punit goyal")

# time.sleep(2)
# Email = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/input[2]").send_keys("punitgoyal106@gmail.com")

# time.sleep(2)
# Phone = driver.find_element(By.ID, "phone")
# Phone.send_keys("9896414101")

# time.sleep(2)
# address = driver.find_element(By.ID, "textarea")
# address.send_keys("Vpo Barwala, near grain market")

# time.sleep(2)
# gender = driver.find_element(By.XPATH, "//*[@id='post-body-1307673142697428135']/div[3]/div[1]")
# gender.click()

# time.sleep(2)
# day = driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[1]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[4]/div[1]")
# day.click()

# time.sleep(2)
# day = driver.find_element(By.XPATH, '//*[@id="post-body-1307673142697428135"]/div[4]/div[5]')
# day.click()


# time.sleep(2)
# country = Select(driver.find_element(By.ID, 'country')).select_by_index(4)
# country = Select(driver.find_element(By.ID, 'country')).select_by_visible_text("France")
# country = Select(driver.find_element(By.ID, 'country')).select_by_value('canada')


# country = Select(driver.find_element(By.ID, 'country')).select_by_visible_text("france")      #error as France not france is present


# colors = Select(driver.find_element(By.ID, 'colors')).select_by_index(4)

# time.sleep(2)
# animals = Select(driver.find_element(By.ID, 'animals')).select_by_value("cheetah")

# time.sleep(2)
# date1 = driver.find_element(By.ID, 'datepicker')
# date1.click()

# time.sleep(4)
# date2 = driver.find_element(By.ID, 'txtDate')
# date2.click()

# time.sleep(2)
# startDate = driver.find_element(By.ID, 'start-date')
# startDate.click()

# time.sleep(2)
# endDate = driver.find_element(By.ID, "end-date")
# endDate.click()

# time.sleep(2)
# button = driver.find_element(By.CLASS_NAME, 'submit-btn')
# button.click()

# time.sleep(2)
# singleFileInput = driver.find_element(By.ID, 'singleFileInput').send_keys(r"G:\MY RESUMES\Punit Resume Updated.pdf")

time.sleep(5)