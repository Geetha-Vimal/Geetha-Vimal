from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Creating an object 'g' of Service class
g = Service("C:\selenium_webdrive\chromedriver.exe")
#Creating a driver and passing the service
driver = webdriver.Chrome(service=g)
#Maximize the window
driver.maximize_window()
#Open the Testing URL
driver.get("https://adactinhotelapp.com/index.php")
#Before thorwing an error it should be wait maximum 10 seconds to load the page
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//*[text()='New User Register Here'").Click()
time.sleep(3)

#Filling the personal details of Register page
driver.find_element(By.NAME,"username").send_keys("geetha13")
driver.find_element(By.NAME,"password").send_keys("geetha@123")
driver.find_element(By.NAME,"re_password").send_keys("geetha@123")
driver.find_element(By.NAME,"full_name").send_keys("Geetha")
driver.find_element(By.NAME,"email_add").send_keys("geethu.1301@gmail.com")

#driver.find_element(By.XPATH,("//*[@id="captcha"]//following::img)).click()

driver.find_element(By.NAME,"captcha").send_keys("crotalo")
driver.find_element(By.NAME,"tnc_box").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[text()='Register'").click()
time.sleep(5)

driver.find_element(By.XPATH,"//button[text()='Click here to login'").click()
driver.refresh()

#Get the Data
username="geetha13"
password="geetha@123"

username_xpath = '/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[2]/td[2]/input'
password_xpath='/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[3]/td[2]/input'
login_button_xpath='/html/body/table[2]/tbody/tr/td[2]/form/table/tbody/tr[6]/td[2]/input'

#find the XPATH of the HTML element present on the webpage
username_xpath=driver.find_element(by=By.XPATH, value=username_xpath)
password_xpath=driver.find_element(by=By.XPATH, value=password_xpath)
login_button_xpath=driver.find_element(by=By.XPATH, value=login_button_xpath)

