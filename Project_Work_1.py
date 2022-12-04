#Name: P Geetha
#Date: 04-12-2022
#Automation Testing with python Selenium
#Project - 1: Develop automation for User Management Tool by adding a user
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Login Details
admin_user = "Admin"
admin_password = "admin123"
first_name = "Geethu13"
last_name = "Ponnam"
full_name = first_name + " "+last_name 
user_name = "geetha11"
password = "Geetha#123"

#Get the URL link and Maximize it
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.maximize_window()

#Login with Admin rights
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(admin_user)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(admin_password)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(5)

#Click to PIM on the left side panel
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
time.sleep(5)

#Again click the Add Employee tab inside the PIM
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a').click()
time.sleep(3)
#Adding First and Last Name
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys(first_name)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys(last_name)
#Save the login details
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]').click()

#Again go to the Admin tab in left side panel
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
time.sleep(2)
#Click the Add user tab in Admin page
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
time.sleep(1)

#Enter the Role
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i').click()
userrolelistbox = driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]')
actions = ActionChains(driver)
actions.move_to_element(userrolelistbox)
Adminelement = driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]/div[2]')
actions.move_to_element(Adminelement).click().perform()

#Add the Employee Name
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').click()
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys(full_name)
time.sleep(2)
WebDriverWait(driver, 10).until(EC.visibility_of(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]')))
time.sleep(1)
actions.move_to_element(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]'))
time.sleep(1)
Emp_Name=driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]/div')
time.sleep(1)
for i in Emp_Name:
    if i.text == full_name:
        actions.move_to_element(i).click().perform()

#Enter the Status
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i').click()
statuslistbox = driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]')
actions = ActionChains(driver)
actions.move_to_element(statuslistbox)
Enabledelement = driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]/div[2]')
actions.move_to_element(Enabledelement).click().perform()

#Calling the Username
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').click()
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys(user_name)

#Calling the Password
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').click()
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys(password)

#Confirm Password
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').click()
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys(password)
time.sleep(3)

#Save the new Employee Login details
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
time.sleep(5)

#Logout from the Admin user
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/p').click()
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()
time.sleep(5)

#Login with Added User Employee
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(user_name)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(password)
driver.find_element(By.XPATH, value= '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(5)

driver.close()
